from os import system
from colorama.initialise import reset_all
from colorama import Fore, Back, Style


class kalkulator:
    def __init__(self,x,y):
        self.A=x
        self.B=y

    def kali(self):
        self.hasil=self.A*self.B
        print(Fore.RED +"Hasil perkalian  : " +str(self.hasil) + Style.RESET_ALL)

    def bagi(self):
        if self.B==0:
            print("Pembagian dengan nol")
        else:
            self.hasil=self.A/self.B
            print(Fore.RED+"Hasil Pembagian : " +str(self.hasil)+ Style.RESET_ALL)

    def tambah(self):
        self.hasil= (self.A) + (self.B)
        print(Fore.RED +"Hasil penjumlahan :" +str(self.hasil) + Style.RESET_ALL)

    def kurang(self):
        self.hasil=self.A-self.B
        print(Fore.RED +"Hasil pengurangan :" +str(self.hasil)+ Style.RESET_ALL)

Pilih = 0
while True:
    print(Fore.CYAN +"\n******KALKULATOR PYTHON******"+ Style.RESET_ALL)
    print("1. Perkalian")
    print("2. Pembagian")
    print("3. Penjumlahan")
    print("4. Pengurangan")
    print("5. Keluar program")
            
    Pilih = input("Masukan pilhan anda : ")
    system('cls')
    if Pilih == "1":
        print("****** PERKALIAN *****")
        a = int(input('\nMasukan Angka Pertama: '))
        b = int(input('Masukan Angka Kedua  : '))
        Object1=kalkulator(a,b)
        Object1.kali()
        kembali=input("\nKlik Enter Untuk Kembali Ke Menu")
        system('cls')

    elif Pilih == '2':
        print(Fore.YELLOW +"****** PEMBAGIAN *****" + Style.RESET_ALL)
        a = int(input('\nMasukan Angka Pertama: '))
        b = int(input('Masukan Angka Kedua  : '))
        Object1=kalkulator(a,b)
        Object1.bagi()
        kembali=input("\nKlik Enter Untuk Kembali Ke Menu")
        system('cls')

    elif Pilih == '3':
        print(Fore.YELLOW +"****** PERTAMBAHAN *****"+ Style.RESET_ALL)
        a = int(input('\nMasukan Angka Pertama: '))
        b = int(input('Masukan Angka Kedua  : '))
        Object1=kalkulator(a,b)
        Object1.tambah()
        kembali=input("\nKlik Enter Untuk Kembali Ke Menu")
        system('cls')
                
    elif Pilih == '4':
        print(Fore.YELLOW+"****** PENGURANGAN *****" +Style.RESET_ALL)
        a = int(input('\nMasukan Angka Pertama: '))
        b = int(input('Masukan Angka Kedua  : '))
        Object1=kalkulator(a,b)
        Object1.kurang()
        kembali=input("\nKlik Enter Untuk Kembali Ke Menu")
        system('cls')

    elif Pilih == '5':
        print("Keluar program")
        print("Terima kasih","\n")
        print("***** ANGGOTA KELOMPOK *****" )
        print(Fore.MAGENTA +"1. Feri Setyawan [5210411173]")
        print("2. Khazin Mubarok [521041187]")
        print("3. Eusebia Nawang Ari [5210411195]")
        print("4. Farel Naufal Azhari [5210411200]")
        break
            
            
    else:
        print(Fore.BLUE+"Maaf,input yang dimasukan salah"+Style.RESET_ALL)
        print ('coba ulangi lagi')

