#Overloading Class ComputerPart

class ComputerPart(): #Class computer
    def __init__ (self,jenis):
        self.jenis = jenis #Atribut public
    
    #function processeor menyimpan parameter nama, harga , pabrikan
    def Processor(self, nama = None, harga = None, pabrikan = None): 
        computerpart_3.display_Computer() #Panggil function display_computer
        print("Nama Processor      : ",nama)
        print("Harga               : ",harga)
        print("Pabrikan            : ",pabrikan,"\n") #\n untuk menambakan enter satu pada saat di run
    
    #function processeor menyimpan parameter nama, harga , pabrikan
    def RandomAccessMemory(self, nama = None, harga = None, pabrikan = None):
        computerpart_1.display_Computer()
        print("Nama RAM            : ",nama)
        print("Harga               : ",harga)
        print("Pabrikan            : ",pabrikan,"\n")

    #function processeor menyimpan parameter nama, harga , pabrikan
    def HardiskSATA(self, nama = None, harga = None, pabrikan = None):
        computerpart_2.display_Computer()
        print("Nama Hardisk        : ",nama)
        print("Harga               : ",harga)
        print("Pabrikan            : ",pabrikan,"\n")
    
    def display_Computer(self): 
        print("Jenis computer part : ",self.jenis)

#Membuat objek
computerpart_1 = ComputerPart("Processor")
computerpart_2 = ComputerPart ("RAM")
computerpart_3 = ComputerPart ("Hardisk")

#Menambahakan Overloading
computerpart_1.Processor("AMD Ryzen 5",1350000,"AMD")
computerpart_2.RandomAccessMemory("KINGSTON HYPERX FURY",365000,"Kingston")
computerpart_3.HardiskSATA("Hardisk WDC Blue",410000,"WD Blue")








