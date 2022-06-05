import cx_Oracle
db = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE")
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Golongan (
	kode_golongan VARCHAR(2),
	nama_golongan VARCHAR(10),
	tunjangan_suami INTEGER(10),
	tunjangan_anak INTEGER(10),
	uang_makan INTEGER(10),
	uang_lembur	INTEGER(10),
	akses INTEGER(10));''')
# INSERT DATA GOLONGAN (INSERT)
cur.execute("INSERT INTO `Golongan` VALUES ('A1', '2D', 600000, 700000, 800000, 300000, 100000)")
cur.execute("INSERT INTO `Golongan` VALUES ('A2', '3A', 400000, 400000, 200000, 100000, 900000)")
cur.execute("INSERT INTO `Golongan` VALUES ('A3', '4B', 300000, 400000, 300000, 200000, 600000)")
db.commit()
# show data table golongan (SELECT)
print("Tabel Golongan")
cur.execute("SELECT * FROM Golongan")
for row in cur.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s" %
        (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
# update Golongan (UPDATE)
cur.execute(
    "UPDATE Golongan SET nama_golongan = '3C' WHERE kode_golongan = 'A1'")
db.commit()
# delete golongan (DELETE)
cur.execute("DELETE FROM Golongan WHERE kode_golongan = '4B' ;")
db.commit()

