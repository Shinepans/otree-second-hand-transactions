from channels.generic.websockets import JsonWebsocketConsumer
from pprint import pprint
import json

replychannels = {}


class ExConsumer(JsonWebsocketConsumer):

    def clean_kwargs(self, pid, pk):
        return {
            'pid': pid,
            'pk': pk
        }

    def connect(self, message, **kwargs):
        kwargs = self.clean_kwargs(**kwargs)
        replychannels[kwargs['pid']] = message.reply_channel
        self.post_connect(**kwargs)

    def post_connect(self, **kwargs):
        pprint(self)
        pass

    def disconnect(self, message, **kwargs):
        kwargs = self.clean_kwargs(**kwargs)
        self.pre_disconnect(**kwargs)

    def pre_disconnect(self, **kwargs):
        pass

    def receive(self, content, **kwargs):
        kwargs = self.clean_kwargs(**kwargs)
        self.post_receive(content, **kwargs)

    def post_receive(self, content, pid, pk):
        pprint(content)
        pprint(pid)
        pprint(pk)
        replychannels[str(pid)].send({'text': json.dumps({
            'msg': 'got msg',
            'back': 'new msg'
        })})
        pass

