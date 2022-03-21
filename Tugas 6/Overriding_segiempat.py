
class Segiempat():
    def __init__(self, panjang, lebar): # methode __init__ menyimpan parameter self,panjang,lebar
        self.panjang = panjang #Atribut public
        self.lebar = lebar  #Atribut public
    
    def hitungLuas(self): # method Overriding
        print("Luas Segiempat     : ", self.panjang * self.lebar, "m^2") # cetak luas segiempat

class Bujursangkar(Segiempat): #Class bujursangkar menyimpan class segiempat
    def __init__(self,sisi):
        self.side = sisi
        Segiempat.__init__(self, sisi,sisi)

    def hitungLuas(self): # Method Overriding
        print("Luas Bujur sangkar : ", self.side*self.side, "m^2")

#Membuat objek (variabel)
b = Bujursangkar(4)
s = Segiempat(2,4)

# Panggil fungction
b.hitungLuas()
s.hitungLuas()