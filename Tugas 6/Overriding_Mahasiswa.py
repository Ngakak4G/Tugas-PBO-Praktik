#Overriding Mahasiswa
class Mahasiswa():   
    def __init__(self,nama,nim):
        self.nama = nama #Atribut Public
        self.nim = nim #Atribut Public
    
    def detSiswa(self):
        print(self.nama, "alamat : Wall Rose") #cetak data dengan panggil atribut publik nama

class Siswa(Mahasiswa):
    def __init__(self,jurusan,nim):
        self.jurusan = jurusan #Atribut Public
        self.nim = nim #Atribut Public

    def detSiswa(self):
        print(self.jurusan,"Jurusan : Informatika") #cetak data dengan panggil atribut publik jurusan

#Membuat objek
mhs1 = Siswa("Mikasa", 135105)
mhs2 = Mahasiswa("Nezuko", 135119)

print(mhs1.nim, mhs2.nama) #cetak data
mhs1.detSiswa() 
print(mhs1.nim, mhs2.nama) 
mhs2.detSiswa() 






