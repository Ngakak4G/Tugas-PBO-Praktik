class Hitung:
    def __init__(self): #Function dengan metode __init__ menyimpan satu parameter (self)
        self.__angkaRahasia = 0 #Atribut bersifat Private

    def tampilkanhitung(self): #Function tampilkan hitung dengan parameter (self)
        self.__angkaRahasia += 1 #Atribut bersifat Private
        print(self.__angkaRahasia)   #cetak atribut  

#panngil function Hitung
hitungan =Hitung()
hitungan.tampilkanhitung()
hitungan.tampilkanhitung()

print(hitungan._Hitung__angkaRahasia)
#cetak

