import cx_Oracle
db = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE"
)
cur = db.cursor()
cur.execute('''
        CREATE TABLE jabatan (
            kode_jabatan VARCHAR (3) NOT NULL PRIMARY KEY,
            nama_jabatan VARCHAR (25),
            gapok INTEGER,
            tunjangan_jabatan INTEGER
        )
        ''')
# INSERT DATA JABATAN (INSERT)
cur.execute("INSERT INTO `jabatan` VALUES ('B1', 'Direktur', 9000000, 6000000)")
cur.execute("INSERT INTO `jabatan` VALUES ('B2', 'HRD', 6000000, 5000000)")
cur.execute("INSERT INTO `jabatan` VALUES ('B4', 'KARYAWAN', 4000000, 4000000)")
db.commit()

# show data table jabatan (SELECT)
print("Tabel Jabatan")
cur.execute("SELECT * FROM jabatan")
for row in cur.fetchall():
    print("%s, %s, %s, %s" %
        (row[0], row[1], row[2], row[3]))

# update jabatan (UPDATE)
cur.execute(
    "UPDATE jabatan SET gapok = 20000000 WHERE kode_jabatan = 'B1'")
db.commit()

# delete jabatan (DELETE)
cur.execute("DELETE FROM jabatan WHERE kode_jabatan = 'B2' ;")
db.commit()
