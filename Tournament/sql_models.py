from flask_sqlalchemy import SQLAlchemy

from demo import trn

DB = SQLAlchemy()


def create_all():
    trn.games_df.to_sql("games", DB.engine)
    trn.players_df.to_sql("players", DB.engine)
    pass
