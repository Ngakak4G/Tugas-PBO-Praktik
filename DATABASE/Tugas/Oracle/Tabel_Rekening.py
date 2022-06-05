import cx_Oracle
db = cx_Oracle.connect(
    "Bank",
    "Bank",
    "127.0.0.1/XE"
)
cur = db.cursor()
# table rekening
cur.execute('''CREATE TABLE IF NOT EXISTS Rekening (
	noRekening VARCHAR(9) PRIMARY KEY,
	pin VARCHAR(6),
	idNasabah VARCHAR(5),
	kodeCabang VARCHAR(3),
	saldo INTEGER,
	FOREIGN KEY(idNasabah) REFERENCES Nasabah(idNasabah),
	FOREIGN KEY(kodeCabang) REFERENCES CabangBank(kodeCabang));''')
# -- INSERT Rekening (INSERT)
cur.execute("INSERT INTO Rekening VALUES ('282908920', '090200', 'KLM01', 'GMB', 1000000);")
cur.execute("INSERT INTO Rekening VALUES ('282820290', '292990', 'PRG02', 'DMS', 9000000);")
cur.execute("INSERT INTO Rekening VALUES ('272980239', '829892', 'RWK03', 'KBM', 5000000);")
db.commit()
# show data rekening (SELECT)
print("\n\nData Rekening")
cur.execute("SELECT * FROM Rekening")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))

# update rekening Bank (UPDATE)
cur.execute(
    "UPDATE Rekening SET saldo = 21500000 WHERE noRekening = '282908920';")
db.commit()


# delete rekening (DELETE)
cur.execute("DELETE FROM Rekening WHERE noRekening = '272980239' ;")
db.commit()