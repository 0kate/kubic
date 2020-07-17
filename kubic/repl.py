import shutil
import sys
from typing import Text

from prompt_toolkit import prompt
from rich import console as rich_console
from rich import table as rich_table

from kubic.command import KubicCommand
from kubic.config import KubicConfig
from kubic.errors import CommandNotFoundError, KubectlNotInstalledError
from kubic.executor import KubicExecutor
from kubic.output import KubicOutput
from kubic.runnable import KubicRunnable
from kubic.translator import KubicTranslator
from kubic.utils import is_command_exists, parse_table_kubectl_returned


class KubicRepl(KubicRunnable):
    """KubicRepl."""

    LABEL = """kubic (kubectl interactive console)
         ___           ___                                     ___     
        /__/|         /__/\         _____        ___          /  /\    
       |  |:|         \  \:\       /  /::\      /  /\        /  /:/    
       |  |:|          \  \:\     /  /:/\:\    /  /:/       /  /:/     
     __|  |:|      ___  \  \:\   /  /:/~/::\  /__/::\      /  /:/  ___ 
    /__/\_|:|____ /__/\  \__\:\ /__/:/ /:/\:| \__\/\:\__  /__/:/  /  /\\
    \  \:\/:::::/ \  \:\ /  /:/ \  \:\/:/~/:/    \  \:\/\ \  \:\ /  /:/
     \  \::/~~~~   \  \:\  /:/   \  \::/ /:/      \__\::/  \  \:\  /:/ 
      \  \:\        \  \:\/:/     \  \:\/:/       /__/:/    \  \:\/:/  
       \  \:\        \  \::/       \  \::/        \__\/      \  \::/   
        \__\/         \__\/         \__\/                     \__\/    
    """

    def __init__(self):
        """__init__."""
        self.console = rich_console.Console()
        self.executor = KubicExecutor()
        self.translator = KubicTranslator()

    def run(self, config: KubicConfig) -> None:
        """run.

        :param config:
        :type config: KubicConfig
        :rtype: None
        """
        if not is_command_exists("kubectl"):
            raise KubectlNotInstalledError()

        # for translator use to determine if the resource name
        self.translator.resources_set = self._get_resources_set()

        print(self.__class__.LABEL)

        while True:
            current_context = self._get_current_context()
            user_input = prompt(f"Context: [{current_context}]\n>> ")

            if not user_input:
                continue

            if user_input in ("exit", "quit"):
                sys.exit(0)

            command = self._translate(user_input)
            try:
                output = self._dispatch(command)
            except CommandNotFoundError:
                print(f"Command {user_input} is not found.\n")
                continue

            self._print(output)

    def _print(self, output: KubicOutput):
        """_print.

        :param output:
        :type output: KubicOutput
        """
        print_method_name = f"_print_{output.kind}_output"

        if hasattr(self, print_method_name):
            print_method = getattr(self, print_method_name)
        else:
            print_method = getattr(self, "_print_other_output")

        print_method(output)

    def _print_get_output(self, output: KubicOutput):
        """_print_get_output.

        :param output:
        :type output: KubicOutput
        """
        RESOURCE_NOT_FOUND_KEYWORD = "No resources"

        if output.text.startswith(RESOURCE_NOT_FOUND_KEYWORD):
            output_contents = output.text
            kwargs = {
                "style": "bold red",
            }
        else:
            table = rich_table.Table(show_header=True, header_style="bold magenta")

            header_row, *item_rows = output.text.split("\n")
            header, items = parse_table_kubectl_returned(header_row, item_rows)

            for col in header:
                table.add_column(col)

            for item in items:
                table.add_row(*item)

            output_contents = table
            kwargs = {}

        self.console.print(output_contents, **kwargs)

    def _print_other_output(self, output: KubicOutput):
        """_print_other_output.

        :param output:
        :type output: KubicOutput
        """
        print(f"{output.text}\n")

    def _dispatch(self, command: KubicCommand) -> KubicOutput:
        """_dispatch.

        :param command:
        :type command: KubicCommand
        :rtype: Text
        """
        return self.executor.run(command)

    def _translate(self, user_input: Text) -> KubicCommand:
        """_translate.

        :param user_input:
        :type user_input: Text
        :rtype: KubicCommand
        """
        return self.translator.run(user_input)

    def _get_resources_set(self) -> set:
        """_get_resources_set.

        :rtype: set
        """
        get_api_resources_command = self._translate("api-resources")
        api_resources_text = self._dispatch(get_api_resources_command).text
        header_row, *api_resource_rows = api_resources_text.split("\n")

        header, api_resources = parse_table_kubectl_returned(
            header_row, api_resource_rows
        )

        api_resources_set = set()
        for api_resource in api_resources:
            api_resource_dict = dict(zip(header, api_resource))

            api_resources_set.add(api_resource_dict["NAME"])
            api_resources_set.add(api_resource_dict["KIND"].lower())
            short_names = api_resource_dict["SHORTNAMES"]
            if short_names:
                api_resources_set.add(short_names)

        return api_resources_set

    def _get_current_context(self) -> Text:
        """_get_current_context.

        :rtype: Text
        """
        get_current_context_command = self._translate("config current-context")
        return self._dispatch(get_current_context_command).text
