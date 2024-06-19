class Produk:
    def __init__(self, nama, harga, stok, kategori):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

    def informasi(self):
        print(f"Informasi Produk:\nNama: {self.nama}\nHarga: Rp{self.harga}\nStok: {self.stok}\nKategori: {self.kategori}")

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        print(f"Stok {self.nama} sekarang: {self.stok}")

    def kurangi_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            print(f"Stok {self.nama} sekarang: {self.stok}")
        else:
            print(f"Stok {self.nama} tidak mencukupi untuk pengurangan sebanyak {jumlah}. Stok saat ini: {self.stok}")

produk1 = Produk("Laptop", 15000000, 15, "Elektronik")
produk2 = Produk("Kursi", 500000, 20, "Furniture")

produk1.informasi()
produk2.informasi()

produk1.tambah_stok(5)
produk2.kurangi_stok(7)
