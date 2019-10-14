import mysql.connector
import socket


class MysqlConfig:
    __instance = None

    @staticmethod
    def getInstance():
        if MysqlConfig.__instance is None:
            MysqlConfig()
        return MysqlConfig.__instance

    def __init__(self):
        if MysqlConfig.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MysqlConfig.__instance = mysql.connector.connect(
               host="192.168.1.7",
               user="root",
               passwd="123",
               auth_plugin='mysql_native_password'
            )
