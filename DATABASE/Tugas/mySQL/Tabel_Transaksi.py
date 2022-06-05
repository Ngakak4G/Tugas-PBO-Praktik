import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Bank')
cur = db.cursor()
# table transaksi
cur.execute('''CREATE TABLE IF NOT EXISTS Transaksi (
	noTransaksi VARCHAR(5),
	jenisNasabah VARCHAR(10),
	idNasabah VARCHAR(5),
	Tanggal DATE,
	jumlah INTEGER);''')
# -- INSERT Transaksi
cur.execute("INSERT INTO Transaksi VALUES ('trans01' , 'Premiun', 'KLM01', date('now'), 10000000);")
cur.execute("INSERT INTO Transaksi VALUES ('trans02' , 'Reguler', 'PRG02', date('now'), 21000000);")
cur.execute("INSERT INTO Transaksi VALUES ('trans03' , 'Reguler', 'RWK03', date('now'), 9000000);")
db.commit()
# # show data transaksi
print("Data Transaksi")
cur.execute("SELECT * FROM Transaksi")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))
# update transaksi
cur.execute("UPDATE Transaksi SET jumlah = 11000000 WHERE idNasabah = 'RWK03';")
db.commit()
# # delete transaksi
cur.execute(
    "DELETE FROM Transaksi WHERE jenisNasabah = 'Premium';")
db.commit()