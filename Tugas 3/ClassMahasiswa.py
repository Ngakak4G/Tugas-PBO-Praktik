class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk =thn_masuk

m1 = Mahasiswa ("Udin","10120371","Sistem Informasi",2020)
# Menambahkan dua objek pada ClassMahasiswa
m2 = Mahasiswa ("Feri Setyawan","5210411173","Informatika",2021)
m3 = Mahasiswa ("Agus Raharjo","5200043511","Teknik Komputer",2019)
daftar_mahasiswa =[m1,m2,m3]
print("***** Daftar Mahasiswa *****","\n")
for y in daftar_mahasiswa:
    teks ="{} adalah mahasiswa {} angkatan {} dengan nim {}".format(y.nama,y.prodi,y.thn_masuk,y.nim)
    print(teks)