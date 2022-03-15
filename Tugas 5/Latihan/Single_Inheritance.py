# Single Inheritance

#Parent Class

class Hewan : #Class Hewan
    def bersuara(self): 
        print("Kucing bersuara") #cetak data

#Child Class mewarsi class Hewan
class Kucing(Hewan): 
    def Suara(self): #Fungction Suara
        print("meong...meong...,meong") #Cetak data

#Menambahkan objek
k = Kucing() #menyimpan class kucing dalam variabel k
k.Suara() #panggil class suara
k.bersuara() #pangil class bersuara

