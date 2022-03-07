class Segitiga: #Class Segitiga
    def __init__(self,alas,tinggi): #Function dengan metode __init__ menyimpan parameter (sels,alas,tinggi)
        self.alas = alas #Atribut Public
        self.tinggi = tinggi #Atribut Public
        self.luas = 0.5 *alas*tinggi #Atribut Public dan menghitung luas segitiga

segitiga_besar = Segitiga(100,80) 
# Mencetak variabel
print("alas   : ", segitiga_besar.alas)
print("tinggi : ", segitiga_besar.tinggi)
print("luas   : ", segitiga_besar.luas)  

