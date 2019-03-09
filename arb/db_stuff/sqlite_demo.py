import sqlite3
from entities import Competitor

#conn = sqlite3.connect('TOURN.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE players (
            name text,
            slackhandle text,
            program text,
            score real
            )""")
# i'''

Player_1 = Competitor('Peyton', '@peyton', 'DS')
Player_2 = Competitor('Ryan H', '@ryanherr', 'OTHER')
Player_3 = Competitor('Troy', '@troy', 'DS')
Player_4 = Competitor('Rudy', '@rudy', 'DS')


def safeinsert(player):
    assert isinstance(player, Competitor)
    valsmap = {
        'name': player.name,
        'username': player.username,
        'program': player.program,
        'score': player.score}
    c.execute(
        "INSERT INTO players VALUES (:name, :username, :program, :score)",
        valsmap)


safeinsert(Player_1)
safeinsert(Player_2)
safeinsert(Player_3)
safeinsert(Player_4)

#c.execute("INSERT INTO players VALUES ('Troy', '@troy', 'DS', '0')")

c.execute("SELECT * FROM players WHERE program=?", ('DS', ))

print(c.fetchall())

conn.commit()

conn.close()
