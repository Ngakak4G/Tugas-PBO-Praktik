import cx_Oracle
db = cx_Oracle.connect(
    "warung",
    "warung",
    "127.0.0.1/XE"
)
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Supplier (
	Kode_Supplier VARCHAR(3) PRIMARY KEY NOT NULL,
	Nama_Supplier VARCHAR(40));''')
# insert data supplier
cur.execute("INSERT INTO Supplier VALUES ('SUP1', 'Johan');")
cur.execute("INSERT INTO Supplier VALUES ('SUP2', 'Wiliam');")
cur.execute("INSERT INTO Supplier VALUES ('SUP3', 'Federick');")
db.commit()
# show supplier
print("Data Supplier")
cur.execute("SELECT * FROM Supplier;")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))
# update supplier
cur.execute(
    "UPDATE Supplier SET Nama_Supplier = 'Asnawai Setyawan' WHERE Kode_Supplier = 'SUP1';")
db.commit()
# delete Supplier
cur.execute("DELETE FROM Supplier WHERE Kode_Supplier = 'SUP2';")
db.commit()