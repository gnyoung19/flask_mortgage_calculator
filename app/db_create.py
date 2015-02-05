# db_create.py 


import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	# get a cursor object used to execute SQL commands
	c = connection.cursor()

	# create the table
	c.execute("""CREATE TABLE mortgages(mortgage_id INTEGER PRIMARY KEY AUTOINCREMENT,
		income INTEGER NOT NULL, down_payment INTEGER NOT NULL, 
		interest_rate INTEGER NOT NULL)""")

	# insert dummy data into the table
	c.execute(
		'INSERT INTO mortgages (income, down_payment, interest_rate)'
		'VALUES(1000, 400, 2)'
	)
	c.execute(
		'INSERT INTO mortgages (income, down_payment, interest_rate)'
		'VALUES(10000, 4000, 4)'
	)