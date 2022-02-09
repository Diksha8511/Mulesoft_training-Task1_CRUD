import sqlite3  #necessary packages imported

connection = sqlite3.connect('movies.db')   # it creates the database
cursor = connection.cursor()

# query to create table
createTableCommand = "CREATE TABLE IF NOT EXISTS details (name TEXT, actor TEXT, actress TEXT, director TEXT, yearOfRelease INTEGER)"
