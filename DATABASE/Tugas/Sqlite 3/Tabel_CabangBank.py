import sqlite3

with sqlite3.connect('bank.db') as db:
    cur = db.cursor()

# table cabang bank (CREATE)
cur.execute('''CREATE TABLE IF NOT EXISTS CabangBank (
	kodeCabang VARCHAR(3),
	namaCabang VARCHAR(60),
	alamatCabang VARCHAR(120));''')
# -- INSERT CabangBank (INSERT)
cur.execute("INSERT INTO CabangBank VALUES ('GMB', 'Cabanng Gombong', 'Gombong kebumen');")
cur.execute("INSERT INTO CabangBank VALUES ('DMS', 'Cabanng Demangsari', 'Ayah kebumen');")
cur.execute("INSERT INTO CabangBank VALUES ('KBM', 'Cabanng Kebumen', 'Kota kebumen');")
db.commit()
# show data cabang bank (SELECT)
print("Data Cabang Bank")
cur.execute("SELECT * FROM CabangBank")
for row in cur.fetchall():
    print("%s ,%s ,%s" % (row[0], row[1], row[2]))

# update cabang bank (UPDATE)
cur.execute(
    "UPDATE CabangBank SET alamatCabang = 'Kecamatan Pejagoan' WHERE kodeCabang = 'GMB'")
db.commit()
# delete cabang bank (DELETE)
cur.execute("DELETE FROM CabangBank WHERE kodeCabang = 'DMS';")
db.commit()