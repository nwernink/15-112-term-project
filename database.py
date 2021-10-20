################################################################################
### THIS FILE CREATED THE USER DATABASE ###
### SQLITE3 WAS LEARNED USING THIS WEBSITE ###
### https://docs.python.org/3/library/sqlite3.html ###
################################################################################

import sqlite3
from cmu_112_graphics import *

conn = sqlite3.connect("user.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE users (
#         username TEXT,
#         password TEXT,
#         account_balance REAL,
#         player_ml REAL,
#         ml_weight
#     )""")

# cursor.execute("INSERT INTO users VALUES ('nick', 'semi', 3989.05, .47, 0)")

# cursor.execute("UPDATE users SET player_ml = 0 WHERE username = 'ngw'")
# cursor.execute("UPDATE users SET account_balance = (?) WHERE username = (?)", (account, user))

for row in cursor.execute('SELECT * FROM users ORDER BY account_balance'):
    print(row)


conn.commit()

conn.close()