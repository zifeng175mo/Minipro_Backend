from ws.consumers import *
from django.conf.urls import url


WEBSOCKET_URL = [
    url(r'^ws/chat/(?P<group_name>[^/]+)/$', ChatConsumer),
    url(r'^ws/push/(?P<username>[0-9a-z]+)/$', PushConsumer),
]
