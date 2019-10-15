import socket


class MysqlConfig:
    __instance = None

    @staticmethod
    def getInstance():
        if MysqlConfig.__instance is None:
            MysqlConfig()
        return MysqlConfig.__instance

    def __init__(self):
        return
