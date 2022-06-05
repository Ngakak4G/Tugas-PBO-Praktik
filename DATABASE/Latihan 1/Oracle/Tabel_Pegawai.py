import cx_Oracle
db = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE"
)
cur = db.cursor()
cur.execute('''
        CREATE TABLE Pegawai (
            nip	VARCHAR (20) NOT NULL PRIMARY KEY,
            nama_pegawai VARCHAR (40),
            kode_jabatan VARCHAR (3),
            kode_golongan VARCHAR (3),
            status VARCHAR (15),
            jumlah_anak INTEGER);''')
# Menanambahkan data (INSERT)
cur.execute("INSERT INTO `Pegawai` VALUES ('922627289', 'Feri Setyawan', 'A1' , '01', 'Mahasiswa', 0)")
cur.execute("INSERT INTO `Pegawai` VALUES ('987654321', 'Adam Mubarok', 'A2' , '02', 'Mahasiswa', 0)")
cur.execute("INSERT INTO `Pegawai` VALUES ('827628249', 'Gunawan', 'A3' , '03', 'Mahasiswa', 0)")
db.commit()
# Menampilkan data (SELECT)
print("Data Tabel pegawai")
cur.execute("SELECT * FROM Pegawai")
for row in cur.fetchall():
    print("%s, %s, %s, %s, %s, %s" %
        (row[0], row[1], row[2], row[3], row[4], row[5]))
# update pegawai (UPDATE)
cur.execute("UPDATE Pegawai SET nama_pegawai = 'Cahyono' WHERE kode_jabatan = 'A3'")
db.commit()
# delete pegawai (UPDATE)
cur.execute("DELETE FROM Pegawai WHERE nip = '987654321' ;")
db.commit()
