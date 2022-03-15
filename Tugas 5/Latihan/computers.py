class ComputerPart(): #Class computer
    def __init__ (self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan #Atribut public
        self.nama = nama 
        self.jenis = jenis 
        self.harga = harga 

class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        #fungsi super untuk mengacu ke kelas induk yaitu class ComputerPart
        super().__init__(pabrikan,nama,"Processor",harga)
        self.jumlah_core = jumlah_core #Atribut public
        self.speed = speed 
#Class RandomAccessMemory dengan menyimpan parameter class ComputerPart
class RandomAccessMemory(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas):
        #fungsi super untuk mengacu ke kelas induk yaitu class ComputerPart
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas #Atribut public

class HardDiskSATA(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
        super().__init__(pabrikan,nama,"SATA",harga)
        self.kapasitas = kapasitas #Atribut public
        self.rpm = rpm #Atribut public
#Membuat objek
p = Processor("Intel","Core i7 7740X",4350000,4," 4.3GHZ")
m = RandomAccessMemory("V-Gen", "DDR4 SODimm PC19200/2400MHZ",328000,"4GB")
hdd = HardDiskSATA("Seagate","HDD 2.5 inch",295000,"5000GB",7200)

parts = [p,m,hdd] #Varibel parts untuk menampung objek
for part in parts: #Mengunakan perulangan for untuk menampilkan data
    print ("{} {} produksi {}".format(part.jenis,part.nama,part.pabrikan)) #Cetak data