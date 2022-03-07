#Semua  variabel bersifat privat
class Mobil(): #Class mobil
    def __init__(self,jendela,pintu,mesin): #Function dengan metode __init__ menyimpan parameter(self,jendela,pintu,mesin)
        self.__jendela = jendela #Atribut private
        self.__pintu = pintu #Atribut private
        self.__mesin = mesin #Atribut private
        
    def tampilkanMobil(self): # untuk menampilkan datanya
        print(f'Mobil Ferrari mempunyai {self.__pintu} pintu dan jendela {self.__jendela} dengan mesin {self.__mesin}') 
print() # untuk menamabahkan jeda atau enter pada saat di run
ferarri = Mobil(2,2, "V8 Turbo 3.855 cc") # Membuat objek dengan nama variabel ferrari
ferarri.tampilkanMobil() #Panggil fungction tampilkan mobil
