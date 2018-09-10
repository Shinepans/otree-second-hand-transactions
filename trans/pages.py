from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree.forms.widgets import _CurrencyInput
from pprint import pprint


class Instructions(Page):
    def vars_for_template(self):
        pprint(vars(self.player))
        return {'name': self.player.name}


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True


class Trans(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
            'name': self.player.name
        }


page_sequence = [
    Instructions,
    ShuffleWaitPage,
    Trans
]
