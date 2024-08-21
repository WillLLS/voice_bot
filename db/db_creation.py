import sqlite3

con = sqlite3.connect('db/database.db')
cur = con.cursor()

# Influencers Table
cur.execute("CREATE TABLE IF NOT EXISTS customers (tm_id TEXT, tm_first_name TEXT, tm_username TEXT, balance INT, total_vocal INT, daily_vocal INT, lt INT, referal_id TEXT)")

cur.execute("CREATE TABLE IF NOT EXISTS referals (referal_id TEXT, tm_id TEXT)")

