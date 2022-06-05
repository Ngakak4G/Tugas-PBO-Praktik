import sqlite3

with sqlite3.connect('bank.db') as db:
    cur = db.cursor()

# table nasabah
cur.execute('''CREATE TABLE IF NOT EXISTS Nasabah ( 
	idNasabah VARCHAR(5) PRIMARY KEY,
	namaNasabah VARCHAR(60),
	alamatNasabah VARCHAR(120));''')

# -- INSERT Nasabah (INSERT)
cur.execute("INSERT INTO Nasabah VALUES ('KLM01', 'John', 'Kec.Sewon');")
cur.execute("INSERT INTO Nasabah VALUES ('PRG02', 'Slamet', 'Kec. Petanahan');")
cur.execute("INSERT INTO Nasabah VALUES ('RWK03', 'Adam', 'Kec. Rowokele');")
db.commit()

# show data nasabah (SELECT)
print("\n\nData Cabang Bank")
cur.execute("SELECT * FROM Nasabah")
for row in cur.fetchall():
    print("%s ,%s ,%s" % (row[0], row[1], row[2]))


# update Nasabah (UPDATE)
cur.execute(
    "UPDATE Nasabah SET namaNasabah = 'John terry' WHERE idNasabah = 'KLM01';")
db.commit()

# delete nasabah (DELETE)
cur.execute("DELETE FROM Nasabah WHERE idNasabah = 'RWK03';")
db.commit()