import os, configparser
from contracts.rabbit_mq_conf import RabbitMQConf

config = configparser.ConfigParser()
config.read('config.conf')

class Config:
    def __init__(self) -> None:
        self.port = config['FLASK']['PORT']
        self.host = config['FLASK']['HOST']
        self.auth_api_url = config["AUTH_API"]["URL"]
        self.auth_api_username = config["AUTH_API"]["USERNAME"]
        self.auth_api_password = config["AUTH_API"]["PASSWORD"]
        # self.store_platform_api_url = config["STORE_PLATFORM_API"]["URL"]

    def rabbit_mq_conf(self) -> RabbitMQConf:
        return RabbitMQConf(
            config['RABBITMQ']['HOST'],
            int(config['RABBITMQ']['PORT']),
            config['RABBITMQ']['USERNAME'],
            config['RABBITMQ']['PASSWORD']
        )