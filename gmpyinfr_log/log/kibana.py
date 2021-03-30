"""
Kibana Logger.
"""

import logging
from io import StringIO

from gmpyinfr_log.log.base import BaseLogger

class KibanaLogger(BaseLogger):
    """
    Implementa um logger baseado no Kibana.
    """

    def __init__(self, filepath, **kwargs):
        """
        Construtor.

        Params:
            - filepath : str indicando o local do arquivo de configuração
            - Recebe os parâmetros de um logging.basicConfig. Confira mais detalhes
            em https://docs.python.org/3/library/logging.html#logging.basicConfig.
        """

        if not filepath:
            raise ValueError("Um arquivo de configuração válido deve ser especificado "
                             "para um logger do tipo Kibana")

        super().__init__(filepath, **kwargs)
        self.server = self.conf['server']
        self.port = self.conf['port']

        self.stream = StringIO()
        self.hs = logging.StreamHandler(self.stream)
        fmt = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
        self.hs.setFormatter(fmt)

        self.logger.addHandler(self.hs)
        self.logger.setLevel(logging.DEBUG)

    def log(self, **kwargs):
        """
        Envia mensagem de log ao logstash.
        """

        print('olha o teste', kwargs)
