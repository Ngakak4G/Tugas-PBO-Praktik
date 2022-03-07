class Utama: #class utama
    def __init__(self): #Function dengan metode __init__ menyimpan parameter self
        self._a = 2 #Atribut protected

class Turunan(Utama): #kelas turunan
    def __init__(self): #Function dengan metode __init__ menyimpan parameter self
        Utama.__init__(self)
        print("Memanggil variablel protected pada class utama : ",self._a) #Memanggil dan mencetak dari fungsi class utama

        #modify the protected variable
        self._a =3
        print("Memanggil variabel protected yang dimodifikasi diluar class : ",self._a)

objek1 = Turunan()
objek2 = Utama()

#Memanggil variabel portected dan mencetaknya
print("Mengakses variabel protected dari objek1 : ",objek1._a)
print("Mengakses variabel protected dari objek2 : ",objek2._a)


