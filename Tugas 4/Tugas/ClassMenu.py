#Class Menu Minuman
class MenuMinuman: 
    def __init__(self,nama,deskripsi,harga,jumlah): #Function yang terdiri dari parameter (nama, deskripsi, harga dan jumlah)
        self.nama = nama #Atrirbut public
        self.deskripsi = deskripsi #Atrirbut public
        self.harga = harga #Atribut public
        self.__jumlah = jumlah #Menambahkan Atribut Private

mnm1 = MenuMinuman("Jus jambu","Jus jambu merah tanpa gula",8500, 3) #Variabel 1
mnm2 = MenuMinuman("Jus alpukat Ori","Jus alpukat dengan tambahan air gula merah", 1500, 1) #Variabel 2
mnm3 = MenuMinuman("Jus alpukat xtra milk","Jus alpukat dengan campuran susu coklat dan taburankeping choco", 15000, 2)# Variabel 2
mnm4 = MenuMinuman("Red & Smooth","Smoothie pisang susu dengan strawberry",17500, 1) #Variabel 3
# Menambahkan dua objek pada class MenuMinuman
mnm5 = MenuMinuman("Es jeruk nipis","jeruk nipis hangat",5000, 2) #Variabel 5
mnm6 = MenuMinuman("Es kelapa muda murni"," Es kelapa muda dengan susu",15000, 1) #Variabel 6

#Variabel untuk menampung semua variabel dalam bentuk LIST
pilihan_minuman =[mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print("Daftar menu Health Fruits") #Cetak 
for mn in pilihan_minuman: #Menggunkan perulangan untuk menampilkan semua data dalam bentuk list
    t = "{} Harga Rp {}, {} {} porsi".format(mn.nama,mn.harga,mn.deskripsi,mn._MenuMinuman__jumlah)
    print(t) #cetak semua datanya (variabel)
