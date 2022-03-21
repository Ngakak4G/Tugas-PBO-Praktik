#Overriding Class ComputerPart

class ComputerPart(): #Class computer atau class induk
    def __init__ (self,pabrikan,harga):
        self.pabrikan = pabrikan #Atribut public
        self.harga = harga 
    
    def display(self): #Function untuk menampilkan data
        print("Pabrikan : ",self.pabrikan) 
        print("Harga    : ", self.harga,"\n") #\n untuk memnambakan enter satu kali ketika di run

class Processor(ComputerPart): 
    def __init__(self,nama,jumlah_core,speed):
        self.nama = nama 
        self.jumlah_core = jumlah_core 
        self.speed = speed 

    def display(self): # Function display untuk menampilkan data
        print("Nama Processor : ",self.nama)
        print("jumlah core    : ",self.jumlah_core)
        print("Speed          : ", self.speed)

#Membuat objek
processor_1 = ComputerPart("Intel", 6000000)
processor_1.display()

# Methode Overriding
# Mengabaikan metode yang dari induk dan mendefinisikan sendiri metode dengan nama yang sama di kelas anak.
# Dan yang dijalankan adalah metode yang ada di kelas anak.
processor_2 = Processor("Intel Core i7",6,"2.4 Ghz")
processor_2.display()


