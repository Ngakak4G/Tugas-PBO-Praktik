# Implementasi Overloading

class Pegawai: #Class pegawai
    jumlah = 0 #Variabel jumlah menyimpan data integer

    def __init__(self, nama, gaji):
        self.nama = nama #Atribut public
        self.gaji = gaji 
        Pegawai.jumlah +=1

    def tampilJumlah(self): 
        print("Total pegawai : ",Pegawai.jumlah) # cetak total pegawai

    def tampilPegawai(self): 
        print("Nama : ", self.nama, ", gaji : ", self.gaji) # cetak nama dan gaji pegawai

    #Method overloading
    def tunjangan(self, istri = None, anak = None): #Function tunjangan
        if anak != None and istri != None:
            #JIka tunjangan ada anak dan istri maka di cetak
            total = anak + istri
            print("Tunjangan anak dan istri : ", total) #Cetak tunjangan anak dan istri

        else: #Jika hanya istri cetak tunjang istri
            total = istri
            print("Tunjangan istri = ", total)

#Memanggil kelas
peg1  = Pegawai("Eren", 2000)
peg2 = Pegawai ("Luffy", 6000)
peg1.tampilPegawai()
peg2.tampilPegawai()
peg1.tunjangan(2500,2000) # Overloading
peg2.tunjangan(2500)      # Overloading

print("Total pegawai %d" % Pegawai .jumlah)
rataGaji = (peg1.gaji + peg2.gaji)/Pegawai.jumlah
print("Rata - rata gaji : "+str(rataGaji)) #cetak data hasil dari variabel rataGaji