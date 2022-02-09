import sqlite3  #necessary packages imported

connection = sqlite3.connect('../movies.db')   # it creates the database
cursor = connection.cursor()

#select query
selectCommand = "SELECT * FROM details where actor = 'Zaheer Iqbal'"

# execute method fires the query that we pass as a parameter
cursor.execute(selectCommand)

movies = cursor.fetchall()
print(movies)