#Multiple Inheritance ComputerPart

class HardDiskSATA_1(): 
    def __init__ (self,nama,pabrikan):
        self.nama = nama 
        self.pabrikan = pabrikan 
    
class HardDiskSATA_2():
    def __init__(self,kapasitas,harga):
        self.kapasitas = kapasitas
        self.harga = harga

class ComputerPart(HardDiskSATA_1,HardDiskSATA_2):
    def __init__(self,nama,pabrikan,kapasitas,harga):
        HardDiskSATA_1.__init__(self,nama,pabrikan)
        HardDiskSATA_2.__init__(self,kapasitas,harga)
        #cetak data
        print()
        print("""SSD {} kapasitas {} harga {} pabrikan dari {}"""
        .format(self.nama, self.kapasitas, self.harga, self. pabrikan))
        
#Membuat objek
ssd = ComputerPart("WD Green SATA","Western Digital","120 GB","Rp.1012000")

