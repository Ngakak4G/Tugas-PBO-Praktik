class MenuMinuman:
    def __init__(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi 
        self.harga = harga

mnm1 = MenuMinuman("Jus jambu","Jus jambu merah tanpa gula",8500)
mnm2 = MenuMinuman("Jus alpukat Ori","Jus alpukat dengan tambahan air gula merah", 1500) 
mnm3 = MenuMinuman("Jus alpukat xtra milk","Jus alpukat dengan campuran susu coklat dan taburankeping choco", 15000)
mnm4 = MenuMinuman("Red & Smooth","Smoothie pisang susu dengan strawberry",17500)
# Menambahkan dua objek pada class MenuMinuman
mnm5 = MenuMinuman("Es jeruk nipis","jeruk nipis hangat",5000)
mnm6 = MenuMinuman("Es kelapa muda murni"," Es kelapa muda dengan susu",15000)

pilihan_minuman =[mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print("Daftar menu Health Fruits")
for mn in pilihan_minuman:
    t = "{} Harga Rp {}, {}".format(mn.nama,mn.harga,mn.deskripsi)
    print(t)