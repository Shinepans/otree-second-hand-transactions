from channels.generic.websockets import JsonWebsocketConsumer
from pprint import pprint
import json
from .models import Player
from .goods_conf import goods

replychannels = {}
goods_list = []

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
        if content['action'] == 'sell_or_buy':
            global goods_list
            all_players_id = [content['id']]
            goods_item = goods[int(content['goods_id'])]
            goods_list.append(goods_item)
            for p in Player.get_others_in_group(Player.objects.get(participant_id=content['id'])):
                all_players_id.append(p.id)
            for id in all_players_id:
                replychannels[str(id)].send({'text': json.dumps({
                    'action': 'syn_sell_list',
                    'sell_list': goods_list
                })})
        pass

