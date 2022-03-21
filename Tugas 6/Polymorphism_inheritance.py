#Polymorhism Inheritance

class Burung:
    def intro(self): #Fungction intro menyimpan parameter self
        print("Di dunia ini ada beberapa type berbeda dari spesies burung") # Cetak

    def terbang(self): #Fungtion terbang menyimpan parameter self
        print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak dapat terbang") #Cetak

class Elang(Burung): #Class Elang dengan menyimpan atau merujuk pada class Burung
    def terbang(self):
        print("Elang dapat terbang") #Cetak

class BurungUnta(Burung):
    def terbang(self): #Fungction terbang menyimpan parameter self
        print("Burung unta tidak dapat terbang")
# Dibuat permisalan dengan variabel untuk setiap class
obj_burung = Burung()
obj_elang = Elang()
obj_burung_unta = BurungUnta()

obj_burung.intro() 

#Panggil class
obj_elang.intro() 
obj_elang.terbang() 

obj_burung_unta.intro() 
obj_burung_unta.terbang()