"""module docstring"""

import pandas as pd
from itertools import permutations
from entities import Bet, Competitor, Forecaster, Game


# an instance of this object for each round
class Round:
    def __init__(self, competitors):
        self.competitors = [Competitor(name) for name in competitors]
        self.advance_to_next = []  # advance to next

    def make_players_df(self):
        dat = {c.name: [c.wins] for c in self.competitors}
        players = pd.DataFrame.from_dict(dat).T
        return players

    def make_games_df(self, mode='exhaustive'):
        '''return list of games for this round.
        mode toggles each player plays once per game or the whole permutation set'''
        n = len(self.competitors)
        if mode == 'exhaustive':
            pairs = permutations(self.competitors, 2)
            games = [Game(ident=i, black=t[0], white=t[1])
                     for i, t in enumerate(pairs)]
        elif mode == 'once':
            assert len(self.competitors) % 2 == 0
            games = [Game(ident=i, black=competitors[k], white=competitors[k + 1])
                     for k in range(0, n // 2, 2)]

        games_dict = {g.ident: [g.black, g.white, g.winner] for g in games}
        games_df = pd.DataFrame.from_dict(games_dict).T.rename(
            columns=['black', 'white', 'winner'])

        return games_df
