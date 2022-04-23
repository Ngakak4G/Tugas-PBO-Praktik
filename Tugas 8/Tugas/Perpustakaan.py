
#Nama = Feri setyawan
#NPM = 5210411173

import datetime
waktu=datetime.datetime.now() 

class Perpusitem: 
    def __init__(self,judul,subjek,lokasi,info):
        self.judul = judul # Atribut Public
        self.subjek =  subjek
        self.lokasi = lokasi
        self.info = info

    '''def lokasiSimpan(self):
    self.lokasi = lokasi
    self.info = info
    '''

class Buku(Perpusitem): 
    def __init__(self,judul,subjek,lokasi,info,isbn,pengarang,jmlhal,ukuran):
        super().__init__(judul,"Buku",lokasi, info) # Fungsi super() digunakan untuk mengacu ke kelas induk dari suatu objek
        self.isbn = isbn
        self.pengarang = pengarang # Atribut public
        self.jmlhal = jmlhal
        self.ukuran = ukuran

class Majalah(Perpusitem): 
    def __init__(self,judul,subjek,lokasi,info,volume,issue):
        super().__init__(judul,"Majalah",lokasi,info) 
        self.volume = volume 
        self.issue = issue

class DVD(Perpusitem): #
    def __init__(self,judul,subjek, lokasi, info, aktor, genre):
        super().__init__(judul,"DVD",lokasi,info) 
        self.aktor = aktor 
        self.fenre = genre

class pinjam(Perpusitem): 
    def __init__(self,nama_buku,pengarang,nama_peminjam, tanggal_pinjam):
        self.nama_peminjam = nama_peminjam
        self.nama_buku = nama_buku # Atribut public
        self.pengarang = pengarang
        self.tanggal_pinjam = tanggal_pinjam

class pengembalian(Perpusitem):
    def __init__(self,nama_buku, pengarang, nama_peminjam, tanggal_pengembalian):
        self.nama_peminjam = nama_peminjam
        self.nama_buku = nama_buku 
        self.pengarang = pengarang
        self.tanggal_pengembalian = tanggal_pengembalian

class katalog(): # class untuk menu pencarian
    def Search(item,my_list):
        found = False
        position = 0
        while position < len(my_list) and not found:
            if my_list[position] == item:
                found = True
            position = position + 1
        return found

#Menambahakan suatu objek
b =Buku("Web Developer","Buku cetak","Rak Nomor 10","dipinjam","945-900-20-02","Ahmad Junaedi",2,"25x110")
m = Majalah("Apa itu Python?","Majalah cetak","Rak nomor 3","ada","X","Bahasa Pemrograman")
d = DVD("Boruto Next Generation","Komik","rak nomor 15","ada","Meski Kodachi","anime")

#  objek buku untuk contoh dalam mesin pencarian
book = ['Sistem operasi','sistem cedas','Front end developer','malin kundang','si kancil']

def buku(): # untuk menampikan objek ketika di run
    daftar =[b,m,d] 
    for dft in daftar: 
        print("Judul  : {}".format(dft.judul))
        print("subjek : {}".format(dft.subjek)) 
        print("Lokasi : {}".format(dft.lokasi)) 
        print("Info   : {}".format(dft.info),"\n") 

#Daftar menu
while True: 
        print("***** PERPUSTAKAAN JENDELA DUNIA *****") 
        print("1. Daftar Buku")
        print("2. Pinjam Buku")
        print("3. Pencarian buku")
        print("4. Pengembalian Buku")
        print("5. Keluar Program")
        pil = 0
        pil =int(input("Masukan Pilihan Anda : ")) #variabel pil untuk memilih menu yang ditampikan


        if pil == 1:
            print("****** DAFTAR BUKU *****")
            buku() #Memanggil function buku yang menmapilkan objek yang tadi sudah dibuat
        
        elif pil == 2:
            print("***** DATA PINJAM BUKU *****")
            nama = str(input("Nama Peminjam  : ")) 
            judul_buku = str(input("Nama Buku      : "))
            pengarang = str(input("Pengarang Buku : "))
            tanggal_pinjam = waktu 

            print("Data pinjam buku berhasil.....","\n")
            print("--------------------------------------------")
    
            p = pinjam(judul_buku,pengarang,nama,tanggal_pinjam) 
            data = [p] # disimpan kedalam variabel data
            for x in data:
                print("Judul buku     : {}".format(x.nama_buku)) 
                print("Karangan       : {}".format(x.pengarang))
                print("Nama           : {}".format(x.nama_peminjam)) 
                print("Tanggal pinjam : {}".format(x.tanggal_pinjam),"\n",) 
            print("--------------------------------------------")

        elif pil == 3:
            print("***** PENCARIAN BUKU *****")
            data =katalog.Search #Variabel data memanggil clas katalog adan function search
            cari = input('Masukan judul Buku : ')
            item =data(cari,book)
            if item:
                print("Buku",cari," berhasil ditemukan....","\n") 
                print('Buku', cari, "Tidak ditemukan....","\n") 

        elif pil == 4: 
            print("***** DATA PENGEMBALIAN BUKU *****") 
            nama = str(input("Nama Peminjam  : ")) 
            judul_buku = str(input("Nama Buku      : ")) 
            pengarang = str(input("Pengarang Buku : "))
            tanggal_pengembalian = waktu 
            print("Data pengembalian buku berhasil.....","\n")
            print("--------------------------------------------")
            p = pengembalian(judul_buku,pengarang,nama,tanggal_pengembalian) 
            for y in data:  
                print("Judul buku     : {}".format(y.nama_buku)) 
                print("Karangan       : {}".format(y.pengarang)) 
                print("Nama           : {}".format(y.nama_peminjam)) 
                print("Dibuat pada    : {}".format(y.tanggal_pengembalian),"\n") 
            print("--------------------------------------------")
        
        elif pil == 5: #
            print("***** KELUAR PROGRAM *****")
            print("Terima Kasih telah berkunjung..............")
            break # untuk 'menghentikan paksa' proses perulangan yang berlangsung
            

        else: 
            print ("<<<<< Maaf menu yang anda pilih tidak ada >>>>>","\n") # mencetak


