#Single inheritance

class Mahasiswa: #Class Mahasiswa
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
    
    def detailMhs(self): #Fungction detailmhs menyimpan parameter self
        return self.nim, self.nama #Mengembalikan nilai nim dan nama
    
    def CekMhs(self): #Fungction CekMhs menyimpan parameter self
        if self.nim <150000: # Jika nilai nim kurang dari 150000 cetk "Mahasiswa Aktif"
            return "Mahasiswa Aktif" #Mengembalikan nilai 
        else: #jika tidak maka "Mahasiswa tidak terdaftar"
            return "Mahasiswa tidak terdaftar " #mMengembalikan nilai

class Siswa(Mahasiswa): #Class siswa menyimpan parameter class Mahasiswa
    def End(self):
        print(" Mahasiswa belum melakukan daftar ulang") #Cetak data
# Objek 1
mahasiswa1 = Mahasiswa("Mahasiswa 1", 135103)
print(mahasiswa1.detailMhs(), mahasiswa1.CekMhs()) #Cetak objek mahasiswa1
# Objek 2
mahasiswa2 = Siswa ("Mahasiwa 2", 150503)
print(mahasiswa2.detailMhs(), mahasiswa2.CekMhs()) #Cetak objek mahasiswa2
mahasiswa2.End()

