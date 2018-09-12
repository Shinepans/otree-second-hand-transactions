from channels.generic.websockets import JsonWebsocketConsumer
from pprint import pprint
import json
from .models import Player
from .goods_conf import goods
from .goods_conf import encode_goods_idx, decode_goods_idx

replychannels = {}
goods_list = []

def findGoods(pid):
    p = Player.objects.get(participant_id=pid)
    p_goods_id_arr = decode_goods_idx(p.goods_id)
    p_goods_arr = []
    for id in p_goods_id_arr:
        p_goods_arr.append(goods[int(id)])
    return p_goods_arr

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
            this_player = Player.objects.get(participant_id=content['id'])
            # update player's goodsID, decode,update,encode
            if goods_item not in goods_list:
                goods_list.append(goods_item)
                this_player_goods_array = decode_goods_idx(this_player.goods_id)
                this_player_goods_array.remove(goods_item['id'])
                this_player.goods_id = encode_goods_idx(this_player_goods_array)
                this_player.save()
            for p in Player.get_others_in_group(this_player):
                all_players_id.append(p.id)
            for pid in all_players_id:
                replychannels[str(pid)].send({'text': json.dumps({
                    'action': 'syn_sell_list',
                    'sell_list': goods_list,
                    'my_goods': findGoods(pid)
                })})
        if content['action'] == 'buy_goods':
            this_player = Player.objects.get(participant_id=content['id'])
            this_player_goods_array = decode_goods_idx(this_player.goods_id)
            this_player_goods_array.append(goods_item['id'])
            this_player.goods_id = encode_goods_idx(this_player_goods_array)
            # TODO find owner; dec my fee, inc his fee
            this_player.save()
        pass

