import sqlite3  #necessary packages imported

connection = sqlite3.connect('../movies.db')   # it creates the database
cursor = connection.cursor()

# insert query
insertCommand = "INSERT INTO details VALUES ('Noteok', 'Zaheer Iqbal', 'Pranutan Bahl', 'Nitin Kakkar', 2019)"

# execute method fires the query that we pass as a parameter
cursor.execute(insertCommand)
connection.commit()
