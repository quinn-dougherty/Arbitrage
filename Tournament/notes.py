from collections import defaultdict
import pandas as pd

from entities import competitor, forecaster, bet, game


class Tournament:
    def __init__(self):
        self.Competitors = pd.DataFrame(columns=['name'])
        self.Forecasters = pd.DataFrame(
            columns=[
                'name',
                'balance',
                'bets_offered_ids',
                'bets_placed_ids'])
        self.Bets = pd.DataFrame(
            columns=[
                'id',
                'game',
                'offered_by',
                'odds',
                'placed_by',
                'money_down',
                'expected_value'])
