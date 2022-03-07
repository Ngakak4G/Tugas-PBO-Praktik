# Semua variabel bersifat public
class Mobil(): #Class Mobil
    def __init__(self,jendela,pintu,mesin): #Fungction yang menyimpan parameter (self,jendela,pintu,mesin)
        self.jendela = jendela #atribut Public
        self.pintu = pintu #atribut Public
        self.mesin = mesin #atribut Public

#Menambahkan objek
avanza = Mobil(4,4,"Toyota")
Pajero = Mobil(4,4,"Mitsubishi")
# Mencetak variabel 
print("***** DAFTAR MOBIL *****","\n")
print("Mobil avanza mempunyai {} jendela dan {} pintu dengan mesin dari {}".format(avanza.jendela,avanza.pintu,avanza.mesin))
print("Mobil pajero mempunyai {} jendela dan {} pintu dengan mesin dari {}".format(Pajero.jendela,Pajero.pintu,Pajero.mesin))

