from flask import Flask, render_template

from .src.toy.demo import trn
from .sql_models import DB


def create_app():
    ''' create and configure an instance of a flask app'''
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def root():
        games = trn.games_df.values
        players = trn.players_df.values
        return render_template(
            'base.html',
            title='home',
            games=games,
            players=players)

    return app
