class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama #Atribut public
        self.nim = nim #Atribut public
        #self.prodi = prodi
        #self.thn_masuk = thn_masuk
        #self.semester = semester

    def tampilMhs(self): #Function untuk menampilkan nama dan nim
        print("Nama : ", self.nama, ", nim : ", self.nim)
    
    #Method Overloading
    def HitungSKS(self, jmlsks = None , sks = None): #Function hitung sks
        if jmlsks != None and sks != None: #JIka ada nilai jumlah sks dan sks maka cetak total sks
            totalsks = jmlsks +sks
            print("Total sks : ",totalsks) # cetak total sks
        else: # jika tidak ada nilai sks maka cetak jumlah sks
            totalsks = jmlsks
            print("Total sks : ", totalsks) #cetak total sks

#Memanggil kelas
mhs1 = Mahasiswa ("Eren" , 123180015) 
mhs2 = Mahasiswa ("Luffy", 123190007)
mhs1.tampilMhs() #Menampilkan data dengan function tampil Mhs
mhs2.tampilMhs()
mhs1.HitungSKS(80, 34) #Overloading
mhs2.HitungSKS(83) #Overloading





