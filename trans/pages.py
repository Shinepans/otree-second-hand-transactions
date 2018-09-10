from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree.forms.widgets import _CurrencyInput
from pprint import pprint
from .goods_conf import decode_goods_idx
from .goods_conf import goods


class Instructions(Page):
    def vars_for_template(self):
        pprint(vars(self.player))
        return {
            'name': self.player.name,
            'fee': self.player.fee
        }


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True


class Trans(Page):
    form_model = 'player'

    def vars_for_template(self):
        goods_id_array = decode_goods_idx(self.player.goods_id)
        goods_array = []
        for g in goods_id_array:
            goods_array.append(goods[int(g)])
        return {
            'name': self.player.name,
            'fee': self.player.fee,
            'goods': goods_array
        }


page_sequence = [
    Instructions,
    ShuffleWaitPage,
    Trans
]
