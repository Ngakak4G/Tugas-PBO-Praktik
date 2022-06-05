import cx_Oracle
db = cx_Oracle.connect(
    "Mahasiswa",
    "Mahasiswa",
    "127.0.0.1/XE"
)
cur.execute('''CREATE TABLE MataKuliah (
    Kode_MK VARCHAR (3) PRIMARY KEY NOT NULL,
    Nama_MK VARCHAR (40),
    SKS VARCHAR (1),
    Semester VARCHAR (1)
)''')
# insert data matakuliah (INSERT)
cur.execute("INSERT INTO MataKuliah VALUES ('MK1', 'Siscom', '2', '1');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK2', 'Siscer', '2', '1');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK3', 'MDPL', '2', '1');")
db.commit()
# Menampilkan data MataKuliah (SELECT)
print(" Data Mata Kuliah")
cur.execute("SELECT * FROM MataKuliah")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
db.commit()
# update data mata kuliah (UPDATE)
cur.execute(
    "UPDATE MataKuliah SET Nama_MK = 'SISTEM CERDAS' WHERE Kode_MK = 'MK2';")
db.commit()
# delete data Mata Kuliah (DELETE)
cur.execute("DELETE FROM MataKuliah WHERE Kode_MK = 'MK1';")
db.commit()