#TIPE DATA SET
a =[10,20,30,20,40]
s =set(a)
print(s)
print(type(s))

#Menambah elemen ke dalam data set
angka ={1,2,3}
angka.add(4)
print(angka)

angka.update([5])
print(angka)

#Menghapus data set
kalimat={"Pemrograman", "Berorientasi", "Objek", "Praktik"}
print(kalimat)

#Menghapus dengan fungsi Remove
kalimat.discard("Praktik")
print(kalimat)
#Menghapus dengan fungsi clear
kalimat.clear()
print(kalimat)

#Menyalin data Set
alfabet ={"A","B","C"}
print(alfabet)
huruf =alfabet.copy()
print(huruf)

#Mencari Irisan atau Intersectioan
data1 ={1,5,3,6}
data2 ={1,5,8,4}
print(data1 & data2)

#Mencari gabungan atau Union
print(data1 | data2)

#Penggunaan Fungsi Frozenset
vokal={"A","I","U","E","O"}
my_set= frozenset(vokal)
print(my_set)