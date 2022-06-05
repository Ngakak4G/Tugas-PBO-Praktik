import sqlite3

with sqlite3.connect('kampus.db') as db:
    cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Kuliah (
    Kode_MK VARCHAR(3) ,
    Kode_Dos VARCHAR(3),
    Waktu TIME,
    Tempat VARCHAR(5),
    FOREIGN KEY(Kode_Dos) REFERENCES Dosen (Kode_Dos),
    FOREIGN KEY(Kode_MK) REFERENCES MataKuliah (Kode_MK)
    );''')
# insert data Kuliah (INSERT)
cur.execute("INSERT INTO Kuliah VALUES ('MK1', 'LK1', '90:40', 'G2.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK2', 'LK2', '13:40', 'G2.4');")
cur.execute("INSERT INTO Kuliah VALUES ('MK3', 'LK3', '09:00', 'G3.3');")
db.commit()
# Menmapilkan data Kuliah (SELECT)
print("\n\nTampilkan data Kuliah")
cur.execute("SELECT * FROM Kuliah")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
db.commit()
# update data Kuliah (UPDATE)
cur.execute(
    "UPDATE Kuliah SET Tempat = 'LC2.3' WHERE Kode_MK = 'MK1';")
# delete data kuliah (DELETE)
cur.execute("DELETE FROM Kuliah WHERE Kode_Dos = 'LK1';")
db.commit()