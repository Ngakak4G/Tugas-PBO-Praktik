import psycopg2
db = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="150202",
    database="kampus"
)
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Kuliah (
    Kode_MK VARCHAR(3) ,
    Kode_Dos VARCHAR(3),
    Waktu TIME,
    Tempat VARCHAR(5)
    );''')
#insert data Kuliah (INSERT)
cur.execute("INSERT INTO Kuliah VALUES ('MK1', 'D21', '09:40', 'G2.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK2', 'D22', '13:40', 'G2.4');")
cur.execute("INSERT INTO Kuliah VALUES ('MK3', 'LK2', '09:00', 'G3.3');")
db.commit()
# Menampilkan data Kuliah (SELECT)
print("Data Kuliah")
cur.execute("SELECT * FROM Kuliah")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
db.commit()
#update data Kuliah (UPDATE)
cur.execute("UPDATE Kuliah SET Tempat = 'LC2.3' WHERE Kode_MK = 'MK1';")
db.commit()
# delete data kuliah (DELETE)
cur.execute("DELETE FROM Kuliah WHERE Kode_Dos = 'LK2';")
db.commit()