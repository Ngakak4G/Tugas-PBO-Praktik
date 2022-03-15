# Multiple Inheritance

class Mahasiswa1(): #Class Mahasiswa1
    def __init__(self,nama,nim): 
        self.nim = nim #Atribut public
        self.nama = nama #Atribut public

class Mahasiswa2():
    def __init__(self,alamat,jurusan):
        self.alamat = alamat #Atribut public
        self.jurusan = jurusan #Atribut public

class Siswa(Mahasiswa1,Mahasiswa2): 
    def __init__(self,nim,nama,alamat,jurusan):
        #Fungction dengan metod __init_ menyimpan parameter self,alamat,jurusan,nim,nama
        Mahasiswa1.__init__(self,nama,nim)
        Mahasiswa2.__init__(self,alamat,jurusan)
print()
#Membuat objek
s = Siswa("Mikasa", 135105,"Wall rose","Informatika")
print("Nim : ",s.nim, "Nama : ",s.nama, "Alamat : ",s.alamat,"Jurusan : ",s.jurusan) #Cetak objek atau data