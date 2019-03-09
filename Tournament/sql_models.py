from flask_sqlalchemy import SQLAlchemy  # type: ignore

from demo import trn  # type: ignore

DB = SQLAlchemy()


def create_all():
    trn.games_df.to_sql("games", DB.engine)
    trn.players_df.to_sql("players", DB.engine)
    pass
