# Polymorphism dengan fungsi

print(len("Polymorphism")) # len untuk mengetahui panjang (jumlah item atau anggota) dari objek
print(len([0,1,2,3]))

# Menggunakan petik tiga (“””) digunakan untuk penulisan paragraf
"""
Menggunakan fungsi len
Output : 12 (Tipe Data String)
4 (Tipe Data List) """

#Using class
class jerman :
    def ibukota(self): #Fungction ibukota dengan parameter self
        print("Berlian adalah ibukota negara Jerman") #cetak

class jepang: #Class Jepang
    def ibukota(self):
        print("Tokyo adalah ibukota negara Jepang")#cetak

#membuat permisalan class dengan variabel
negara1 = jerman()
negara2 = jepang()

for country in (negara1,negara2): #Menggunkan perulangan for untuk mencetak dalam bentuk list
    country.ibukota() #Panggil function ibukota