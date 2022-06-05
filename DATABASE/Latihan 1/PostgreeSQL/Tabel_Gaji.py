import psycopg2
db = psycopg2.connect(user="postgres",
    password="150202",
    host="localhost",
    database="data")
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Gaji (
	bulan	VARCHAR(20),
	nip	VARCHAR(20),
	masuk	INTEGER(5),
	sakit	INTEGER(5),
	ijin	INTEGER(5),
	alpha	INTEGER(5),
	lembur	INTEGER(5),
	potongan	INTEGER(10));''')
# Menambahkan  data Gaji (INSERT)
cur.execute("INSERT INTO `Gaji` VALUES ('Januari', '1829373890', 20, 0, 3, 1, 1, 60000)")
cur.execute("INSERT INTO `Gaji` VALUES ('Februari', '1820282729', 20, 1, 1, 4, 2, 90000)")
cur.execute("INSERT INTO `Gaji` VALUES ('Maret', '335456353', 23, 4, 0, 0, 2, 80000)")
db.commit()
# menampilkan data  gaji (SELECT)
print("Tabel Gaji")
cur.execute("SELECT * FROM Gaji")
for row in cur.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s, %s" %
        (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
# update data gaji (UPDATE)
cur.execute("UPDATE Gaji SET masuk = 25, sakit = 1, ijin = 2 , alpha = 3 WHERE bulan= 'Januari'")
db.commit()
# delete  gaji (DELETE)
cur.execute("DELETE FROM Gaji WHERE bulan = 'Februari' ;")
db.commit()