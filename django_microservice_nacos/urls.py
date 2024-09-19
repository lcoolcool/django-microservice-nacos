import socket
from django.urls.conf import path
from django_microservice_nacos.nacos import nacos
from django.http import HttpResponse


def get_network_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('1.1.1.1', 80))
    __ip__ = s.getsockname()[0]
    s.close()

    return __ip__


def nacos_beat_view(request):
    nacos.client.send_heartbeat(nacos.data_id, get_network_ip(), "8000", group_name=nacos.group)
    return HttpResponse(status=200)


urlpatterns = [
    path('beat/', nacos_beat_view)
]
