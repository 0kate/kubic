import subprocess


class KubicExecutor(object):
    def get_kubectl_config(self): 
        config = subprocess.check_output(['kubectl', 'config', 'view'])
        return config
