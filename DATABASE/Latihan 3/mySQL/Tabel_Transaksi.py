import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Warung"
)
cur.execute('''CREATE TABLE IF NOT EXISTS Transaksi_Barang (
	No_Nota VARCHAR(3),
	Kode_Barang VARCHAR(3),
	Qty INTEGER(3),
	Harga INTEGER,
	FOREIGN KEY(No_Nota) REFERENCES Nota(No_Nota),
	FOREIGN KEY(Kode_Barang) REFERENCES Barang(Kode_Barang));''')
# insert transakasi barang (INSERT)
cur.execute("INSERT INTO Transaksi_Barang  VALUES ('001', 'A01', 1, 14000000);")
cur.execute("INSERT INTO Transaksi_Barang  VALUES ('002', 'A02', 2, 15000000);")
cur.execute("INSERT INTO Transaksi_Barang  VALUES ('003', 'A03', 3, 16000000);")
db.commit()
# show transaksi barang (SELECT)
print("Data Transaksi Barang")
cur.execute("SELECT * FROM Transaksi_Barang ;")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
# update transaksi barang (UPDATE)
cur.execute(
    "UPDATE Transaksi_Barang  Harga = 12000000 WHERE Kode_Barang = 'A01';")
db.commit()
# delete transaksi barang (DELETE)
cur.execute("DELETE FROM Transaksi_Barang WHERE No_Nota = '002';")
db.commit()
