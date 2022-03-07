#Class Buku
class Buku:
    #Function yang terdiri dari parameter(judul,pengarang, tahun terbit, penerbit buku)
    def __init__(self,judul,pengarang,tahun_terbit,penerbit_buku): 
        self.judul = judul #Atribute public
        self.pengarang = pengarang #Atribute public
        self.tahun_terbit = tahun_terbit #Atribute public
        #Menambahkan atribut Private
        self.__penerbit_buku = penerbit_buku
buku = Buku("Tenggelamnya Kapal Van der Wijck", "HAMKA", 1938,"Centrale Courant") #Variiabel 1 yang menampung parameter
# Menambhakan dua objek pada classBuku
cerpen = Buku("Negeri Kabut","Seno Gumira Ajidarma", 1999,"Grasindo") #Variiabel 2 yang menampung parameter
novel = Buku("Ronggeng Dukuh Paruk","Ahmad Tohari",1982,"Gramedia Pustaka Utama") #Variiabel 3 yang menampung parameter
#Untuk menamapung semua variabel dalam bentuk data List
list_buku = [buku, cerpen, novel]
print("***** Daftar Buku *****","\n")
for x in list_buku: #Menggunkan perulangan for untuk memanggil dalam bentuk list
    t = "Buku {} karangan {} pertama kali diterbitkan tahun {} yang diterbitkan oleh {} ".format(x.judul,x.pengarang,x.tahun_terbit,x._Buku__penerbit_buku)
    print(t) #cetak