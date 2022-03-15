# Hierachical Inheritance

#Class parent atau class induk
class Induk:
    def fungsiinduk(self): #
        print("Fungsi pada parent class")#cetak

#Class turunan 1
class Anak1(Induk): 
    def fungsianak1(self):
        print("Fungsi pada anak 1.") #cetak

#Class turunan 2
class Anak2(Induk): 
    def fungsianak2(self): 
        print("Fungsi pada anak 2.") #cetak

a1 = Anak1() #panggil class anak1 disimpan dalam variabel a1
a2 = Anak2() #panggil class anak2 disimpan dalam variabel a2

a1.fungsiinduk() #Panggil fungsiinduk variabel a1
a1.fungsianak1() ##Panggil fungsiinduk variabel a2

a2.fungsiinduk() #Panggil fungsiinduk variabel a2