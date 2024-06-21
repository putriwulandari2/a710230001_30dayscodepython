class Toko:
    def __init__(self, nama, lokasi, jenis_toko):
        self.nama = nama
        self.lokasi = lokasi
        self.jenis_toko = jenis_toko
        self.pendapatan = 0
        self.produk_terjual = 10

    def informasi(self):
        print(f"Informasi Toko:\nNama: {self.nama}\nLokasi: {self.lokasi}\nJenis Toko: {self.jenis_toko}\nPendapatan: Rp{self.pendapatan}\nProduk Terjual: {self.produk_terjual}")

    def tambah_pendapatan(self, jumlah, jumlah_produk_terjual):
        self.pendapatan += jumlah
        self.produk_terjual += jumlah_produk_terjual
        print(f"Pendapatan {self.nama} bertambah Rp{jumlah} dari penjualan {jumlah_produk_terjual} produk.")

    def kurangi_pendapatan(self, jumlah, jumlah_produk_terjual):
        if self.pendapatan >= jumlah and self.produk_terjual >= jumlah_produk_terjual:
            self.pendapatan -= jumlah
            self.produk_terjual -= jumlah_produk_terjual
            print(f"Pendapatan {self.nama} berkurang Rp{jumlah} dari pengembalian {jumlah_produk_terjual} produk.")
        else:
            print(f"Pengurangan pendapatan atau produk terjual tidak dapat dilakukan. Pendapatan saat ini: Rp{self.pendapatan}, Produk terjual saat ini: {self.produk_terjual}")

toko1 = Toko("Uniqlo", "Mall Solo Paragon", "Toko Baju")
toko2 = Toko("Toko Buku Gramedia", "Solo Square", "Toko Buku")

toko1.informasi()
toko2.informasi()

toko1.tambah_pendapatan(5000000, 100)  
toko2.kurangi_pendapatan(3000000, 50)  
