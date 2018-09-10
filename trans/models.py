from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)
from pprint import pprint
import random

players_name = ['Li', 'Pan', 'Chen', 'Wang', 'Guo', 'Lu', 'Wan']

class Constants(BaseConstants):

    # otree structs vars
    name_in_url = 'trans'
    players_per_group = 2
    num_rounds = 1

    # self defined vars
    goods = [
        {
            '1': {
                'name': 'Dell Xps 13',
                'price': 5399
            }
         },
        {
            '2': {
                'name': 'Apple Data Line',
                'price': 100
            }
        },
        {
            '3': {
                'name': 'Iphone X',
                'price': 5899
            }
        },
        {
            '4': {
                'name': 'Dog Xiao hua',
                'price': 3000
            }
        },
        {
            '5': {
                'name': 'Dog Xiao Jin',
                'price': 4000
            }
        },
        {
            '6': {
                'name': 'Cat Miao',
                'price': 2000
            }
        },
        {
            '7': {
                'name': 'Cat Haha',
                'price': 1000
            }
        },
        {
            '8': {
                'name': 'Diamond',
                'price': 4000
            }
        },
        {
            '9': {
                'name': 'Huawei P20',
                'price': 4000
            }
        },
        {
            '10': {
                'name': 'Glass Cup',
                'price': 30
            }
        },
        {
            '11': {
                'name': 'PC',
                'price': 5000
            }
        },
        {
            '12': {
                'name': 'Book A',
                'price': 50
            }
        },
        {
            '13': {
                'name': 'Kindle',
                'price': 1200
            }
        },
        {
            '14': {
                'name': 'VIP Account',
                'price': 360
            }
        }
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            # init players' random name
            random_idx = int(random.random()*(len(players_name)))
            # init the fee of 3000-5999
            random_fee = 6000 - int(random.random()*3000)
            p.fee = random_fee
            p.name = players_name[random_idx]
            del players_name[random_idx]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField
    fee = models.IntegerField

