class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, jumlah_halaman):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.jumlah_halaman = jumlah_halaman

    def informasi(self):
        print(f"Informasi Buku:\nJudul: {self.judul}\nPengarang: {self.pengarang}\nTahun Terbit: {self.tahun_terbit}\nJumlah Halaman: {self.jumlah_halaman}")

    def tambah_halaman(self, tambahan):
        self.jumlah_halaman += tambahan
        print(f"Jumlah halaman {self.judul} sekarang: {self.jumlah_halaman}")

buku1 = Buku("Anak Kost-Kostan", "Serena Tria", 2009, 341)
buku2 = Buku("Suara dari Dilan", "Pidi Baiq", 2016, 360)

buku1.informasi()
buku2.informasi()
buku1.tambah_halaman(50)
