import sqlite3

with sqlite3.connect('db\data.db') as db:
    cur = db.cursor()
#Membuat Tabel dalam Database (Create)
cur.execute('''CREATE TABLE IF NOT EXISTS jabatan (
    kode_jabatan VARCHAR(3),
    nama_jabatan VARCHAR(40),
    gapok INTEGER(10),
    tunjangan_jabatan INTEGER(10)
);''')

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
