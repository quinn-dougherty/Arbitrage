from boards import Boards
from entities import Competitor, Forecaster, Game, Bet
from utils import show
from random import randint
from typing import List, Dict
from fractions import Fraction as ratio
import pandas as pd

idspace = 4


class Book(Boards):
    def __init__(self, competitors: str, usernames: str, sections: str):
        super().__init__(competitors, usernames, sections)
        self.forecasters = {'HOUSE': Forecaster('HOUSE', balance=1000)}
        self.bets = self.init_H0()
        self.bettors = self.bettors_df(self.forecasters)
        self.book_df = self.make_bets_df()

    def make_forecaster(self, name: str, username='', program='', balance=100):
        """we can admit new forecasters on a rolling basis"""
        self.forecasters[name] = Forecaster(name, username, program, balance)
        self.bettors = self.bettors_df(self.forecasters)
        pass

    def bettors_df(self, bettors: Dict[str, Forecaster]):
        '''represent the table of bettors'''
        dat = {name: [bettors[name].name, bettors[name].username]
               for name in bettors.keys()}
        bettorsdf = pd.DataFrame.from_dict(dat,
                                           orient='index',
                                           columns=['balance', 'username'])
        return bettorsdf

    def init_H0(self) -> List[Bet]:
        ''' The house initializes each player at a null hypothesis. '''
        identifiers = [randint(10**idspace, 10**(idspace + 1))
                       for _ in range(len(self.competitors))]
        while len(set(identifiers)) != len(identifiers):
            identifiers = [randint(10**idspace, 10**(idspace + 1))
                           for _ in range(len(self.competitors))]
        bets = {identi: Bet(ident=randint(10**idspace, 10**(idspace + 1)),
                            posted_by=self.forecasters['HOUSE'],
                            odds=ratio(1, 1), on=name, amount=2)
                for identi, name in zip(identifiers, self.competitors.values())}
        return bets

    def make_bets_df(self):
        ''' shows a df of the bets'''
        dat = {
            b.ident: [
                b.posted_by,
                b.odds,
                b.on,
                b.amount,
                b.taken_by] for b in self.bets.values()}
        book_df = pd.DataFrame.from_dict(
            dat, orient='index', columns=[
                'posted_by', 'odds', 'on', 'amount', 'taken_by'])
        return book_df

    def show_avail_bets(self):
        '''returns a DF of bets, hiding the ones that have already been taken '''
        return self.book_df[self.book_df.taken_by.apply(
            lambda f: f.name) == "NOBODY"].applymap(show)

    def show_taken_bets(self):
        '''returns a DF of bets, ONLY the ones that have already been taken '''
        return self.book_df[self.book_df.taken_by.apply(
            lambda f: f.name) != "NOBODY"].applymap(show)

    def post_bet(self, posted_by, odds, on, amount):
        x = randint(10**idspace, 10**(idspace + 1))
        while x in self.book_df.index:
            x = randint(10**idspace, 10**(idspace + 1))
        assert x not in self.book_df.index
        self.bets[x] = (Bet(ident=x,
                            posted_by=self.forecasters[posted_by],
                            odds=odds,
                            on=self.competitors[on],
                            amount=amount))
        self.book_df = self.make_bets_df()
        pass

    def take_bet(self, by, ident):
        taken_by = self.forecasters[by]
        assert isinstance(taken_by, Forecaster)
        self.bets[ident].taken_by = taken_by
        self.book_df = self.make_bets_df()
