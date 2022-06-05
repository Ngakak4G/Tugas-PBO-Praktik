import sqlite3

with sqlite3.connect('toko.db') as db:
    cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Barang (
	Kode_Barang VARCHAR(3),
	Nama_Barang VARCHAR(40));''')

# insert barang (INSERT)
cur.execute(
    "INSERT INTO Barang VALUES ('A01', 'ASUS ROG');")
cur.execute(
    "INSERT INTO Barang VALUES ('A02', 'LENOVO Thinkpad');")
cur.execute(
    "INSERT INTO Barang VALUES ('A03', 'Thosiba');")
db.commit()
# show barang (SELECT)
print("\n\nData Barang")
cur.execute("SELECT * FROM Barang;")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))
    
# update barang (UPDATE)
cur.execute(
    "UPDATE Barang SET Nama_Barang = 'MACBOOK M1' WHERE Kode_Barang = 'A02'; ")
db.commit()
# Delete Barang (DELETE)
cur.execute("DELETE FROM Barang WHERE Kode_Barang = 'A02';")
db.commit()