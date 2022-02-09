#Menghitung Volume Balok

print("***** MENGHITUNG LUAS KERUCUT ***** ","\n")
phi = 3.14
r =int(input("Masukan nilai Jari-jari     : "))
s =int(input("Masukan nilai garis pelukis : "))
t =int(input("Masukan nilai tinggi        : "))

Luas = (phi*(r*r)) + (phi*r*s)
print()
print("_____________________________________")
print("Jadi Luas kerucutnya adalah : ",Luas)
#Membulatkan bilangan dengn library round
pembulatan =round(Luas)
print("Dibulatkan menjadi    `      : ",pembulatan)