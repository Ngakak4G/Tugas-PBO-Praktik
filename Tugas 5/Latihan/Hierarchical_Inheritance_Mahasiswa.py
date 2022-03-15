# Hierachical Inheritance  class mahasiswa

class Mahasiswa: #Class mahasiswwa
    def __init__(self,nama,nim): 
        self.nama = nama #Atribut public
        self.nim = nim #Atribut public

class Siswa1(Mahasiswa):
    def __init__(self,nama,nim): 
        self.nama = nama #Atribut public
        self.nim = nim #Atribut public

    def detSiswa1(self): 
        print (self.nama, "alamat : Wall rose")

class Siswa2 (Mahasiswa): #Class Siswa2  menyimpan parameter class Mahasiswa
    def __init__(self,nama,nim): 
        self.nama = nama #Atribut public
        self.nim = nim 
        
    def detSiswa2(self):  #Fungction detSiswa2 menyimpan parameter self
        print(self.nama, "Jurusan : Informatika") #cetak atribut nama
#Membuat objek mhs1 dan mhs2
mhs1 = Siswa1 ("Mikasa", 135105)
mhs2 = Siswa2 ("Nezuko", 1351117)

print(mhs1.nim) #cetak mhs1 dengn atribut nim
mhs1.detSiswa1() #panggil fungction detSiswa1
print(mhs2.nim) #cetak mhs2 dengn atribut nim
mhs2.detSiswa2() #panggil fungction detSiswa2