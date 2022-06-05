import sqlite3

with sqlite3.connect('bank.db') as db:
    cur = db.cursor()
# table transaksi
cur.execute('''CREATE TABLE IF NOT EXISTS Transaksi (
	noTransaksi VARCHAR(5) PRIMARY KEY,
	jenisNasabah VARCHAR(10),
	idNasabah VARCHAR(5),
	tanggal DATE,
	jumlah INTEGER,
	FOREIGN KEY(idNasabah) REFERENCES Nasabah(idNasabah));''')
# -- INSERT Transaksi
cur.execute("INSERT INTO Transaksi VALUES ('trans01' , 'Premiun', 'KLM01', date('now'), 10000000);")
cur.execute("INSERT INTO Transaksi VALUES ('trans02' , 'Reguler', 'PRG02', date('now'), 21000000);")
cur.execute("INSERT INTO Transaksi VALUES ('trans03' , 'Reguler', 'RWK03', date('now'), 9000000);")
db.commit()
# show data transaksi
print("Data Transaksi")
cur.execute("SELECT * FROM Transaksi")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))
# update transaksi
cur.execute(
    "UPDATE Transaksi SET jumlah = 10000000 WHERE noTransaksi = 'trx01' AND idNasabah = 'PML01';")
db.commit()
# delete transaksi
cur.execute(
    "DELETE FROM Transaksi WHERE noTransaksi = 'trx05' AND idNasabah = 'BDG01';")
db.commit()