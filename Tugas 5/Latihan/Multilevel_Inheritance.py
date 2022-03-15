#Multilevel Inheritance

#Parent Class
class Hewan : #Class Hewan
    def bersuara(self): 
        print("Kucing bersuara") #cetak

#Child class mewarisi class hewan
class Kucing(Hewan): 
    def suara(self): #Fungction suara dengan parameter self
        print("meong...meong...meong") #cetak
#Child class mewarisi dari class Hewan
class AnakKucing(Kucing):
    def minum(self):
        print("Minum susu") #Cetak

#objek
ak = AnakKucing() 
ak.bersuara() #panggil fungction bersura
ak.suara() #panggil fungction bersura
ak.minum() #panggil fungction minum

