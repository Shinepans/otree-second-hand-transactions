from channels.routing import route
from myapp.consumers import ws_add, ws_disconnect
from otree.channels.routing import channel_routing

channel_routing += [
    route("websocket.connect", ws_add, path=r"^/chat"),
    route("websocket.disconnect", ws_disconnect, path=r"^/chat"),
]