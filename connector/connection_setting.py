import mysql.connector

#
#mysql = MySQL(config.config)
#mysql.conn

class MySQL():
    def __init__(self, config):
        u"""
        :param config: setting connection
        """
        self.config = config
        self.conn = None
        if config is not None:
            self.connect()

    def connect(self, config=None):
        u"""
        :return: connection
        """
        if config is None:
            config = self.config
        conn = mysql.connector.connect(**config)
        self.conn = conn
        return conn