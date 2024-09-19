import json

from nacos import NacosClient
from django.conf import settings


class Nacos(object):
    def __init__(self):
        super().__init__()
        self._client = None

    @property
    def client(self):
        if self._client:
            return self._client
        self._client = NacosClient(
            settings.NACOS_SERVER_ADDRESSES,
            namespace=settings.NACOS_SERVER_NAMESPACE,
            username=settings.NACOS_SERVER_USERNAME,
            password=settings.NACOS_SERVER_PASSWORD
        )
        return self._client

    @property
    def data_id(self):
        return settings.NACOS_SERVER_DATA_ID

    @property
    def group(self):
        return settings.NACOS_SERVER_GROUP if hasattr(settings, 'NACOS_SERVER_GROUP') else "DEFAULT_GROUP"


nacos = Nacos()


def get_json_config():
    return nacos.client.get_config(data_id=nacos.data_id, group=nacos.group)


def get_config():
    return json.loads(get_json_config())
