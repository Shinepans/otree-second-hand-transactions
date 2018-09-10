from channels.generic.websockets import JsonWebsocketConsumer

replychannels = {}

# TODO


class ExConsumer(JsonWebsocketConsumer):

    def clean_kwargs(self, player_id, pk):
        return {
            'player_id': player_id,
            'pk': pk
        }

    def connect(self, message, **kwargs):
        kwargs = self.clean_kwargs(**kwargs)
        replychannels[kwargs['player_id']] = message.reply_channel
        self.post_connect(**kwargs)

    def post_connect(self, **kwargs):
        pass

    def disconnect(self, message, **kwargs):
        kwargs = self.clean_kwargs(**kwargs)
        self.pre_disconnect(**kwargs)

    def pre_disconnect(self, **kwargs):
        pass

    def receive(self, content, **kwargs):
        kwargs = self.clean_kwargs(**kwargs)
        self.post_receive(content, **kwargs)

    def post_receive(self, content, player_id, pk):
        pass

