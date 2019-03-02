"""module docstring"""
from itertools import permutations
from typing import List, Dict, Optional
from numpy.random import permutation as shuff_idx
import pandas as pd
import altair as alt

from entities import Bet, Competitor, Forecaster, Game
from utils import show, DF, Chart

## global vars
lose_val, draw_val, win_val = (0, 0.5, 1)


class Boards:
    def __init__(
            self,
            competitors: List[str],
            usernames: List[str],
            sections: List[str],
            mode=1):
        assert len(competitors) == len(usernames) == len(sections)
        self.competitors = {
            name: Competitor(
                name, un, section) for name, un, section in zip(
                competitors, usernames, sections)}
        self.games_df = self.make_games_df()
        self.players_df = self.make_players_df()

    def make_players_df(self) -> DF:
        '''represent the table of players'''
        dat = {c.name: [c.score] for c in self.competitors.values()}
        players = pd.DataFrame.from_dict(
            dat, orient='index', columns=['score'])
        return players

    def make_games_df(self):
        '''return list of games
        double round robin'''

        n = len(self.competitors)
        pairs = permutations(self.competitors.values(), 2)
        games = [Game(ident=i, black=t[0], white=t[1])
                 for i, t in enumerate(pairs)]

        games_dict = {g.ident: [g.black, g.white, g.winner] for g in games}
        games_df = pd.DataFrame.from_dict(games_dict, orient='index', columns=[
            'black', 'white', 'winner']).loc[shuff_idx(range(len(games)))]

        games_df.index = pd.RangeIndex(1, games_df.shape[0] + 1)

        return games_df

    def mark_winner(self, ident, victory):
        '''say who won which game (white, black, or draw)

        updates both games board and players board'''
        if victory == 'black':
            loser = 'white'
            self.games_df.iloc[ident].winner = self.games_df.iloc[ident][victory]
            self.players_df.loc[self.games_df.iloc[ident]
                                [victory].show()] += win_val
            self.players_df.loc[self.games_df.iloc[ident]
                                [victory].show()] += lose_val
        elif victory == 'white':
            loser = 'black'
            self.games_df.iloc[ident].winner = self.games_df.iloc[ident][victory]
            self.players_df.loc[self.games_df.iloc[ident]
                                [victory].show()] += win_val
            self.players_df.loc[self.games_df.iloc[ident]
                                [victory].show()] += lose_val
        else:
            self.games_df.winner.iloc[ident] = 'draw'
            self.players_df.loc[self.games_df.iloc[ident]
                                ['white'].show()] += draw_val
            self.players_df.loc[self.games_df.iloc[ident]
                                ['black'].show()] += draw_val
        pass

    def show_scores(self, expect: Optional[str] = "NULL") -> Chart:
        """ show current scores"""
        C = alt.Chart(self.players_df.reset_index()).mark_bar().encode(
            x='index:N',
            y=alt.Y('score:Q', sort="ascending"),
            color=alt.condition(
                alt.datum.score > 3.5,
                alt.value('orange'),
                alt.value('steelblue')
            )
        )
        return C
