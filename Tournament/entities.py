"""entities"""
import typing
from fractions import Fraction as ratio
from utils import Person


class Competitor(Person):
    def __init__(self, name, username='', program='OTHER'):
        super().__init__(name, username, program)
        self.score = 0


class Forecaster(Person):
    def __init__(self, name, username='', program='OTHER', balance=100):
        super().__init__(name, username, program)
        assert isinstance(balance, (int, float))
        self.balance = balance
        self.bets_offered = None
        self.bets_taken = None

    def show(self):
        return (self.name, self.balance)


class Game:
    def __init__(self, ident, black, white, winner=None):
        assert isinstance(black, Competitor)
        assert isinstance(white, Competitor)
        if winner is None:
            winner = Competitor("NOBODY")
        assert isinstance(winner, Competitor)
        self.ident = ident
        self.black = black
        self.white = white
        self.winner = winner


class Bet:
    '''TODO: update all the stuff for game_id param.

    Factor out the emtpy forecaster and the empty competitor into somewhere else.
    '''

    def __init__(
            self,
            ident: int,
            game_id: int,
            posted_by: Forecaster,
            odds: ratio,
            on: Competitor,
            amount: float,
            taken_by=None):
        assert amount <= posted_by.balance
        if taken_by is None:
            taken_by = Forecaster("NOBODY", balance=0)
        assert isinstance(taken_by, Forecaster)
        self.ident = ident
        self.posted_by = posted_by
        self.odds = odds
        self.on = on
        self.amount = amount
        self.taken_by = taken_by
        self.implicit_forecast = self.report_implicit_forecast()

    def report_implicit_forecast(self):
        s0 = f'{self.posted_by.show()} would like to bet ${self.amount} on {self.on.show()} at {self.odds.numerator} to {self.odds.denominator} odds.\n'
        if self.taken_by is None:
            s1 = ''
        else:
            s1 = f'{self.taken_by.show()} has accepted these odds and posted this money. '

        return s0 + s1
