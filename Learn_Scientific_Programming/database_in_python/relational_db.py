import sqlite3

con = sqlite3.connect('animal.sqlite')

if con:
    print("Koneksi berhasil.")
else:
    print("Koneksi gagal.")


curr = con.cursor()
# curr.execute(
#     '''SELECT * FROM bird_cage''')
curr.execute(
    '''SELECT * FROM bird_cage JOIN bird ON bird_cage.cage_id = bird.cage_id WHERE bird_cage.cage_id = 1''')
for row in curr:
    print(row)
