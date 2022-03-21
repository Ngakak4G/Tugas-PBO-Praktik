# Polymorphism dengan class
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama #Atribut Public
        self.umur = umur 

    
    def bersuara(self): #Function bersuara
        print("Meow") # cetak

class Dog():
    def __init__(self, nama, umur):
        self.nama = nama #Atribut Public
        self.umur = umur

    def bersuara(self):
        print("Guk..guk..") #Cetak

#Mebyuat objek dsimpan dalam sebuah variabel
kucing1 = Kucing("Tom", 3) #Variabel 1
anjing1 = Dog("Spike", 4) #Variabel w2

#Menggunakan perulangn for yang menyimpan variabel  kucing1 dan anjing1
for hewan in (kucing1, anjing1): 
    hewan.bersuara() # panggil function bersuara dengan variabel hewan.