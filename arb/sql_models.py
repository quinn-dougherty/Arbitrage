from flask_sqlalchemy import SQLAlchemy  # type: ignore
from . import APP  # type: ignore
from .src.toy.demo import trn  # type: ignore

DB = SQLAlchemy()
'''
class Players(DB.Model):
    #id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(50), primary_key=True, nullable=False)
    username = DB.Column(DB.String(40), nullable=True)
    section = DB.Column(DB.String(10), nullable=True)
    score = DB.Column(DB.Float, nullable=False)
    '''


def create_all():
    trn.games_df.to_sql("games", DB.engine)
    trn.players_df.to_sql("players", DB.engine)
    pass
