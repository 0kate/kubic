import subprocess


class KubicExecutor(object):
    KUBECTL = 'kubectl'

    def get_kubectl_config(self): 
        config = subprocess.check_output([self.__class__.KUBECTL, 'config', 'view'])
        return config
