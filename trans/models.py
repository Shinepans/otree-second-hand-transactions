from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)
from pprint import pprint
import random
from .goods_conf import goods
from .goods_conf import encode_goods_idx
from .goods_conf import decode_goods_idx

players_name = ['Li', 'Pan', 'Chen', 'Wang', 'Guo', 'Lu', 'Wan']

class Constants(BaseConstants):

    # otree structs vars
    name_in_url = 'trans'
    players_per_group = 4
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):

        # define players' name and fee, init players' goods
        players_goods = []
        for p in self.get_players():
            # init players' random name
            random_idx = int(random.random()*(len(players_name)))
            # init the fee of 3000-5999
            random_fee = 6000 - int(random.random()*3000)
            random_name = players_name[random_idx]
            del players_name[random_idx]
            p.fee = random_fee
            p.name = random_name
            players_goods.append([])

        # define players' goods
        for g in goods:
            all_players = self.get_players()
            chosed = int(random.random()*len(all_players))
            players_goods[chosed].append(g['id'])
        # encode goods id for players
        players = self.get_players()
        for goods_array_idx in range(len(players_goods)):
            players[goods_array_idx].goods_id = encode_goods_idx(players_goods[goods_array_idx])



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    fee = models.IntegerField()
    goods_id = models.StringField()
