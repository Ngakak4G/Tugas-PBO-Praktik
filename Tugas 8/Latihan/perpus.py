class Perpusitem:
    def __init__(self,judul,subjek,lokasi,info):
        self.judul = judul
        self.subjek =  subjek
        self.lokasi = lokasi
        self.info = info

    '''def lokasiSimpan(self):
    self.lokasi = lokasi
    self.info = info
    '''

class Buku(Perpusitem):
    def __init__(self,judul,subjek,lokasi,info,isbn,pengarang,jmlhal,ukuran,nama):
        super().__init__(judul,"Buku",lokasi, info,nama)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran

class Majalah(Perpusitem):
    def __init__(self,judul,subjek,lokasi,info,volume,issue):
        super().__init__(judul,"Majalah",lokasi,info)
        self.volume = volume
        self.issue = issue

class DVD(Perpusitem):
    def __init__(self,judul,subjek, lokasi, info, aktor, genre):
        super().__init__(judul,"DVD",lokasi,info)
        self.aktor = aktor
        self.genre = genre

class pengarang:
    def __init__(self,nama):
        self.nama = nama

b =Buku("Pemrograman python","Buku cetak","Rak Nomor 1","dipinjam","945-884-98-02","Yogi syarif",2,"25x15")
m = Majalah("Dunia komputer","Majalah cetak","Rak nomor 2","ada","VII","Komputer")
d = DVD("Shingek no kyojin","softcopy","rak nomor 3","ada","mikasa","anime")

daftar =[b,m,d]
for dft in daftar:
    print('{} {} {} {}'.format(dft.judul,dft.subjek,dft.lokasi,dft.info))