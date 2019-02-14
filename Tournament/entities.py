"""entities"""
import typing


class Competitor:
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        self.wins = 0

    def show(self): 
        return self.name

class Forecaster:
    def __init__(self, name, balance):
        assert isinstance(name, str)
        self.name = name
        self.balance = 100
        self.bets_offered = None
        self.bets_taken = None

    def show(self):
        return (self.name, self.balance)

class Game:
    def __init__(self, ident, black, white, winner=None):
        assert isinstance(black, Competitor)
        assert isinstance(white, Competitor)
        self.ident = ident
        self.black = black
        self.white = white
        self.winner = winner

class Bet:
    '''NOTE: You have to split this into "bets posted" and "bets taken" '''

    def __init__(
            self,
            ident,
            game,
            offered_by,
            odds,
            max_cash,
            taken_by,
            money_down=0,
            expected_value=None):
        assert isinstance(ident, int)
        assert isinstance(game, Game)
        assert isinstance(offered_by, Forecaster)
        assert isinstance(max_cash, (int, float))
        assert isinstance(taken_by, Forecaster)
        self.ident = ident
        self.game = game
        self.bettor = offered_by
        self.bettee = taken_by
        self.money_down = money_down

# NOTE
