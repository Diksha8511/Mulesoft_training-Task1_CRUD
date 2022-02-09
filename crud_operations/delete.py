import sqlite3  #necessary packages imported

connection = sqlite3.connect('../movies.db')   # it creates the database
cursor = connection.cursor()

#delete query
deleteCommand = "DELETE FROM details WHERE name = 'test'"

# execute method fires the query that we pass as a parameter
cursor.execute(deleteCommand)
connection.commit()