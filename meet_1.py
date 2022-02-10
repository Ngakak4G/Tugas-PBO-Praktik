def luaskerucut():
    print("----- MENGITUNG LUAS KERUCUT -----")
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
    print("Dibulatkan menjadi          : ",pembulatan)

def volumekerucut():
    print("----- MENGHITUNG VOLUME KERUCUT -----")
    phi = 3.14
    r = int(input("Masukan nilai Jari Jari  : "))
    t = int(input("Masukan nilai tinggi     : "))

    volume = (1/3*phi*r*r*t)
    print()
    print("_____________________________________")
    print("Jadi Luas kerucutnya adalah : ",volume)
    #Membulatkan bilangan dengn library round
    pembulatan =round(volume)
    print("Dibulatkan menjadi          : ",pembulatan)

while True:
    print("***** MENGHITUNG Bangun KERUCUT ***** ","\n")
    print("1. Hitung Luas bangun kerucut")
    print("2. Hitung Volume kerucut")
    print("3. Keluar program")
    pilihan = int(input("Masukan pilihan anda : "))
    print()

    if pilihan == 1:
        luaskerucut()
    elif pilihan == 2:
        volumekerucut()
    elif pilihan == 3:
        print("Keluar Program")
        print("5210411173 Feri Setyawan")
        break    
    else:
        print("Angka yang diinputkan salah")



