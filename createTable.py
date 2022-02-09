import sqlite3  #necessary packages imported

connection = sqlite3.connect('movies.db')   # it creates the database
cursor = connection.cursor()
