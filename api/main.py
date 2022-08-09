from leanapi.server import ApiServer

from api.core.app_config import AppConfig
from api.modules import modules


def start():
    server = ApiServer.config(configs=AppConfig.load()).loads(modules).server()

    server.start()


if __name__ == "_main_":
    start()
else:
    server = ApiServer.config(configs=AppConfig.load()).loads(modules).server()
    app = server
