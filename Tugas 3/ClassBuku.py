class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku = Buku("Tenggelamnya Kapal Van der Wijck", "HAMKA", 1938)
# # Menambhakan dua objek pada classBuku
cerpen = Buku("Negeri Kabut","Seno Gumira Ajidarma", 1999)
novel = Buku("Ronggeng Dukuh Paruk","Ahmad Tohari",1982)
list_buku = [buku, cerpen, novel]
print("***** Daftar Buku *****","\n")
for x in list_buku:
    t = "Buku {} karangan {} pertama kali diterbitkan tahun {}".format(x.judul,x.pengarang,x.tahun_terbit)
    print(t)