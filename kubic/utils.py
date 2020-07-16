import shutil
from typing import Text


def is_command_exists(command: Text):
    """is_command_exists.

    :param command:
    :type command: Text
    """
    return shutil.which(command) is not None


def parse_table_kubectl_returned(header, contents):
    """parse_table_kubectl_returned.
    parse table that kubectl returned. (etc. "kubectl api-resources")
    separate column by header width. (separate point: 'v')
    ===================================================================================================
    v                                vv           vv                             vv           vv      v
    NAME                              SHORTNAMES   APIGROUP                       NAMESPACED   KIND
    bindings                                                                      true         Binding
    ===================================================================================================

    :param header:
    :param contents:
    """
    i, column_start_points = 0, []
    while i < len(header):
        if header[i] != " ":
            column_start_points.append(i)
            while i < len(header) and header[i] != " ":
                # for skip current column name
                i += 1
        # for skip space
        i += 1

    parsed_header = [
        header[column_start_points[i]:column_start_points[i+1]].strip()
        for i in range(len(column_start_points)-1)
    ]
    # for last column
    parsed_header.append(header[column_start_points[-1]:len(header)].strip())

    parsed_contents = []
    for content in contents:
        parsed_content = [
            content[column_start_points[i]:column_start_points[i+1]].strip()
            for i in range(len(column_start_points)-1)
        ]
        parsed_content.append(content[column_start_points[-1]:len(content)].strip())
        # for last column
        parsed_contents.append(parsed_content)

    return parsed_header, parsed_contents
