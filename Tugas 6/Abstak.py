
from abc import ABC, abstractmethod 
class Bentuk(ABC):
    @abstractmethod # abstractmethod  metode yang dideklarasikan, tetapi tidak mengandung implementasi.
    def luas(self): #Function luas
        return self.__sisi * self.__sisi

    @abstractmethod
    def Keliling(self): #Function Keliling
        return 4 * self.__sisi #Retrun nilai

#Class persegi menyimpan class bentuk
class Persegi(Bentuk):
    def __init__(self,sisi):
        self.__sisi = sisi #Atribut public
    def luas(self):  #Function luas
        return self.__sisi * self.__sisi 
    def Keliling(self):
        return 4 * self.__sisi
#Membuat objek
persegi = Persegi(6) #variabel 
print(persegi.luas()) #panggil Function luas dalam variabel persegi
print(persegi.Keliling()) #panggil Function keliling dalam variabel persegi