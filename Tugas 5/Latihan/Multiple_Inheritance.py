# Multiple Inheritance
#Parent 1 atau class induk 1
class Perhitungan1: #Class perhitungan1
    def penjumlahan(self,a,b): 
        return a+b #mengembalikan nilai a ditambah nilai b

#Parent 2
class Perhitungan2:#Class perhitungan2
    def perkalian(self,a,b):
        return a*b #mengembalikan nilai a dikalikan nilai b

# Child
#Class hitung menyimpan parameter  class perhitungan1 dan class perhitungan2
class Hitung(Perhitungan1, Perhitungan2):
    def pembagian(self,a,b): 
        return a/b #mengembalikan nilai a dibagi nilai b

#Membuat objek
h= Hitung() #Vaiabel h menyimpan class hitung
print("Penjumlahan : ",h.penjumlahan(20,30)) #Cetak function penjumlahan
print("Perkalian : ",h.perkalian(2,4)) #Cetak function perkalian
print("Pembagian : ",h.pembagian(6,12)) #Cetak function pembagian

