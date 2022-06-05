import psycopg2

db = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="150202",
    database="kampus"
)
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Dosen (
    Kode_Dos VARCHAR(3) ,
    Nama_Dos VARCHAR(40),
    Alamat_Dos VARCHAR(125),
    No_Telp VARCHAR(15)
    );''')
# insert data dosen (INSERT)
cur.execute("INSERT INTO Dosen VALUES ('D21', 'Slamet', 'Bogor', '283493048');")
cur.execute("INSERT INTO Dosen VALUES ('D22', 'Ridwan', 'Bekasi', '363439843');")
cur.execute("INSERT INTO Dosen VALUES ('LK2', 'Agung', 'Bantul', '2473284782');")
db.commit()
# Menampilkan data Dosen (SELECT)
print("Tampilkan data Dosen")
cur.execute("SELECT * FROM Dosen")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
db.commit()
# update data Dosen (UPDATE)
cur.execute("UPDATE Dosen SET Nama_Dos = 'Aji Santoso' WHERE Kode_Dos = 'LK2';") 
db.commit()
# delete data Dosen (DELETE)
cur.execute("DELETE FROM Dosen WHERE Kode_Dos = 'D22';")
db.commit()