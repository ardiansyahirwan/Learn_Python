import sqlite3

connection = sqlite3.connect('animal.sqlite')

# cursor = connection.cursor()

# cursor.execute(
#     "INSERT INTO bird_cage (cage_id, cage_name) VALUES (?,?)", (None, 'Love Bird'))
# connection.commit()

# cursor.execute("SELECT bird_name, qty FROM bird")
# for (k, v) in cursor:
#     print(k, v)
# connection.close()
# cursor.execute("DROP TABLE IF EXISTS bird_cage")
# cursor.execute(
#     "CREATE TABLE bird_cage (cage_id INTEGER PRIMARY KEY AUTOINCREMENT, cage_name TEXT)")

# connection.close()
