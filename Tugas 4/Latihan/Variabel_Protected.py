# Semua variabel bersifat protected
class Mobil(): #Class Mobil
    def __init__(self,jendela,pintu,mesin): #Function dengan metode __init__ (self,jendela,pintu,mesin)
        self._jendela = jendela #Atribut Private
        self._pintu = pintu #Atribut Private
        self._mesin = mesin #Atribut Private

class Truk(Mobil): #Class truk menyimpan parameter mobil
    def __init__(self,jendela,pintu,mesin,tipe):
        super().__init__(jendela,pintu,mesin) #fungsi super untuk mengacu ke kelas induk yaitu class mobil
        self._tipebak = tipe #Variabel

    def tampil(self): # Fungction untuk menampilkan datanyaZ
        #akses class truk
        print(f'Mobil ini mempunnyai {self._jendela} jendela {self._pintu} pintu dengan mesin {self._mesin} tipe {self._tipebak}')
jeep = Truk(2,2,"diesel","Honda") #Membuat objek dari kelas mobil
print()
jeep.tampil() #panggil fungction tampil


