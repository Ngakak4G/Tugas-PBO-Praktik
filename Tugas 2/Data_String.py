#TIPE DATA STRING
str1 = "aku cinta indonesia"
print(str1)

str2 = str1[:10]+'tanah airku'+str1[9:]
print(str2)

str3 = 'aku cinta tanah air ku indonesia'
str4 = str3[:9]+''+str3[22:]
print(str4)

kelas = 'Praktikum Pemrograman Berorientasi Objek'
up = kelas.upper()
lo = kelas.lower()
print(kelas)
print(up)
print(lo)

s = '     python     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(len(kelas))

jumlah = len(kelas)
print('panjang string adalah :',jumlah)

s1 = 'python '
s2 = 'programing'
print(s1+s2)

print(kelas.index('a'))
print(kelas)

kelas2 = kelas.replace('Praktikum','praktik')
print(kelas2)

a = 'satu'
b = 'dua'
c = 'tiga'
print('saya mempunyai %s mangga'%(b))

print(kelas.split())

input1 = input('hari ini adalah : ')
print(input1)

data1 = input('angka 1 : ')
data2 = input('angka 2 : ')
data3 = int(data1)+int(data2)
print(data1,' * ',data2,' = ',data3)