import cx_Oracle

db = cx_Oracle.connect(
    "warung",
    "warung",
    "127.0.0.1/XE"
)
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Nota (
	No_Nota VARCHAR(3) PRIMARY KEY,
	Tanggal date,
	Tempo VARCHAR(10),
	Total INTEGER(10),
	Kode_Supplier VARCHAR(3),
	FOREIGN KEY(Kode_Supplier) REFERENCES Supplier(Kode_Supplier));''')
# insert data Nota (INSERT)
cur.execute("""INSERT INTO Nota VALUES ('001' ,date('now'), 'Senin', 5000000, 'SUP1');""")
cur.execute("""INSERT INTO Nota VALUES ('002' ,date('now'), 'Selasa',6000000, 'SUP2');""")
cur.execute("""INSERT INTO Nota VALUES ('003' ,date('now'), 'Rabu', 7000000, 'SUP3');""")
db.commit()
# show nota (SELECT)
print("Data Nota")
cur.execute("SELECT * FROM Nota;")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))
# update Nota (UPDATE)
cur.execute("UPDATE Nota SET Total = 70000000 WHERE No_Nota = '002';")
db.commit()
# delete Nota (DELETE)
cur.execute("DELETE FROM Nota WHERE No_Nota = '001';")
db.commit()