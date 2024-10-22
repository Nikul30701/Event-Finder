import  sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("gata.db")
cursor = connection.cursor()

# Query  all data based on condition
cursor.execute("SELECT * FROM event WHERE date='2022.10.10'")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT band, date FROM event WHERE date='2022.10.10'")
rows = cursor.fetchall()
print(rows)

#  Insert new rows
new_rows = [('Cat', 'Cat City', '2022.10.17'),
            ('Donkey', 'Donkey City', '2022.10.17')]

cursor.executemany("INSERT INTO event VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM event")
rows = cursor.fetchall() # it always return a list of string with execute
# and with executemany it always return a list of tuple.
print(rows)
