#Multilevel Inheritance class mahasiswa
class Mahasiswa:#Class mahasiswa
    def __init__(self,nama,nim): 
        self.nama = nama #Atribut public
        self.nim = nim 

class Siswa1(Mahasiswa): #Class Siswa1 menyimpan parameter class mahasiswa
    def __init__(self,nama,nim): 
        self.nama = nama #Atribut public
        self.nim = nim 

class Siswa2(Siswa1): #Class Sisw21 menyimpan parameter class siswa1
    def __init__(self,nama,nim):
        self.nama = nama #Atribut public
        self.nim = nim 

#Membuat objek mhs1, mhs2, mhs3
mhs1 = Mahasiswa("Mikasa", 135105)
mhs2 = Siswa1 ("Nezuko", 135117)
mhs3 = Siswa2 ("Hancock", 134079)

#Cetak data
print(mhs1.nama, mhs1.nim)
print(mhs2.nim)
print(mhs3.nama)

