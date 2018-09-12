from trans.consumers import ExConsumer
from otree.channels.routing import channel_routing
from channels.routing import route_class

ex_path = r"^/ex/(?P<pid>\w+)/(?P<pk>\w+)$"

channel_routing += [
    route_class(ExConsumer, path=ex_path),
]