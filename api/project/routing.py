"""
Websocket url mapping file.
"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import ws.routing

APPLICATION = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ws.routing.WEBSOCKET_URL
        )
    ),
})
