from __future__ import absolute_import
import csv
import os
from fractions import Fraction as ratio
from typing import Dict
from random import sample

from ..book import Book
PLAYERS = os.path.abspath('Tournament/src/toy/' + 'players.csv')


def make_book(filename) -> Book:

    with open(filename) as tsv:
        vals = {}
        for column in zip(*[line for line in csv.reader(tsv, delimiter='\t')]):
            vals[column[0]] = list(column[1:])

    return Book(vals['player_name'], vals['username'], vals['program'])


def mark_w_random_wins(n: int, t: Book):
    assert 3 * n < t.games_df.shape[0]

    for k in range(n):
        t.mark_winner(k, 'black')
        t.mark_winner(k + n, 'draw')
        t.mark_winner(k + 2 * n, 'white')
    pass


def post_random_bets(t: Book):

    t.make_forecaster("angela", 'angela')
    t.make_forecaster("hermione")
    t.make_forecaster("dma", 'dma')
    t.post_bet('dma', ratio(4, 1), "Ryan Allred", 4)
    t.post_bet('dma', ratio(9, 1), "Troy Bradley", 1)
    t.post_bet('hermione', ratio(3, 1), "Pierre Damiba", 9)

    x = sample(list(t.bets.keys()), 9)

    t.take_bet('hermione', x[0])
    t.take_bet('dma', x[1])
    t.take_bet('hermione', x[2])
    t.take_bet('hermione', x[3])
    t.take_bet('angela', x[4])
    pass


abspath_playerscsv = PLAYERS

trn = make_book(abspath_playerscsv)

mark_w_random_wins(9, trn)

post_random_bets(trn)
