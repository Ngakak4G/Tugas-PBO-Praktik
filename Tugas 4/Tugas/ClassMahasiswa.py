class Mahasiswa: #kelas Mahasiswa
    def __init__(self,nama,nim,prodi,thn_masuk,daerah): #Function dengan metode __init__ yang
        # menyimpan parameter (self,nama,nim,prodi,thn_masuk)
        self.nama = nama #Atribut public
        self.nim = nim #Atribut public
        self.prodi = prodi #Atribut public
        self.thn_masuk =thn_masuk #Atribut public
        #Menambahkan atribut private
        self.__daerah = daerah

m1 = Mahasiswa ("Udin","10120371","Sistem Informasi",2020,"Jakarta") #Variabel 1
# Menambahkan dua objek pada ClassMahasiswa
m2 = Mahasiswa ("Feri Setyawan","5210411173","Informatika",2021,"Kebumen") #Variabel 2
m3 = Mahasiswa ("Agus Raharjo","5200043511","Teknik Komputer",2019,"Bandung") #Variabel 3
#Menampung vaiabel ke dalam bentuk data List
daftar_mahasiswa =[m1,m2,m3]
print("***** Daftar Mahasiswa *****","\n")
for y in daftar_mahasiswa: #Menggunakan perulangan for untuk memanggil
    teks ="{} adalah mahasiswa {} angkatan {} dengan nim {} asal daerah {}".format(y.nama,y.prodi,y.thn_masuk,y.nim,y._Mahasiswa__daerah)
    print(teks) #cetak

    