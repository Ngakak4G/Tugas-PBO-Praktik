#Fungsi private dan public

class pegawai: #Class Pegawai
    __nama = "" #atribut private
    __alamat = "" #atribut private
    __gaji = "" #atribut private

    def __init__(self,nama,alamat): #Function dengan metode __init__ menyimpan parameter (self,nama,alamat)
        self.__nama = nama #atribut private
        self.__alamat = alamat #atribut private
    
    def __hitungGaji(self): #Function hitung gaji menyimpan parameter (self)
        upahLembur = 20000 #variabel dan baiaya upah lembur
        gajipokok = 2000000 #variabel dan baiaya gaji pokok
        jumlahLembur = int(input("Total jam lembur : ")) #User menginputkan jumlah lembur
        self.__gaji=(upahLembur*jumlahLembur)+gajipokok #Menjumlahkan semua upah lembur dan gaji pokok

    def tampilDetail(self): #Function tampil detail menyimpan parameter (self) #untuk menampilkan data
        print("\n--Menghitunng dan Menampilkan Detail Gaji Pegawai--")
        print("Nama : ",self.__nama) #Mencetak nama dari atribut private
        print("Alamat : ",self.__alamat) #Mencetak alamat dari atribut private
        self.__hitungGaji() #Memanggil function hitung gaji
        print("Total Gaji : ",self.__gaji) #mencetak total gaji

#Membuat Objek Pegawai
pgw1 = pegawai ("Mikasa Ackerman", "Wall Rose") 
pgw1.tampilDetail() #Memanggil function tampil detail

pgw2 = pegawai("Saya Kisaraagi","Prefektur Nagano")
pgw2.tampilDetail() #Memanggil function tampil detail