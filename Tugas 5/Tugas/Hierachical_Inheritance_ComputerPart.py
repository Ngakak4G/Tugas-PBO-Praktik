#Hierachical Inheritance ComputerPart

class ComputerPart(): #Class computer
    #Fungction dengan metode __init__ menyimpan parameter(self,pabrikan,nama,jenis,harga)
    def __init__ (self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan #Atribut public
        self.nama = nama #Atribut public
        self.jenis = jenis #Atribut public
        self.harga = harga #Atribut public
#Class porcessor dengan menyimpan parameter class ComputerPart
class Processor(ComputerPart):
    #Fungction dengan metode __init__ menyimpan parameter(self,pabrikan,nama,harga,jumlah_core,speed)
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        #fungsi super untuk mengacu ke kelas induk yaitu class ComputerPart
        super().__init__(pabrikan,nama,"processor",harga)
        self.jumlah_core = jumlah_core #Atribut public
        self.speed = speed #Atribut Public

#Class RandomAccessMemory dengan menyimpan parameter class ComputerPart
class RandomAccessMemory(ComputerPart):
    #Fungction dengan metode __init__ menyimpan parameter((self,pabrikan,nama,harga,kapasitas)
    def __init__(self,pabrikan,nama,harga,kapasitas):
        #fungsi super untuk mengacu ke kelas induk yaitu class ComputerPart
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas #Atribut public
#Class HardDiskSATA dengan menyimpan parameter class ComputerPart
class HardDiskSATA(ComputerPart):
    #Fungction dengan metode __init__ menyimpan parameter(self,pabrikan,nama,harga,kapasitas,rpm)
    def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
        super().__init__(pabrikan,nama,"SATA",harga)
        self.kapasitas = kapasitas #Atribut public
        self.rpm = rpm #Atribut public
print("*****SPESIFIKASI COMPUTER*****","\n")
def display_processor():
    p =Processor("AMD","AMD Ryzen 5 2600",2050000,6,"3.4 GHz")
    print ("""Processor {} jumlah core {} harga {} kecepatan {} produksi dari {}"""
        .format(p.nama,p.jumlah_core,p.harga,p.speed,p.pabrikan)) #Cetak data
display_processor() #panggil fungction untuk menampilkan data

def display_ram():
    r =RandomAccessMemory("Kingston FURY IMPACT ",8,795000,"Kingston")
    print ("""Ram {} dengan kapasitas {} GB harga Rp.{} produk dari {}"""
        .format(r.nama,r.kapasitas,r.harga,r.pabrikan)) #Cetak data
display_ram() #panggil fungction untuk menampilkan data

def display_HDD():
    h =HardDiskSATA("HDD Seagate Barracuda",500,7200,199000,"Seagate Indonesia")
    print ("""Ram {} dengan kapasitas {} GB rpm {}  harga Rp.{} produk dari {}"""
        .format(h.nama,h.kapasitas,h.harga,h.rpm,h.pabrikan)) #Cetak data
display_HDD() #panggil fungction untuk menampilkan data








