class Buah:
    def __init__(self, nama, harga_per_kg, stok):
        self.nama = nama
        self.harga_per_kg = harga_per_kg
        self.stok = stok
    
    def update_harga(self, harga_baru):
        self.harga_per_kg = harga_baru
        print(f"Harga {self.nama} diperbarui menjadi ${self.harga_per_kg} per kg.")
    
    def tambah_stok(self, tambahan):
        self.stok += tambahan
        print(f"{tambahan} kg {self.nama} ditambahkan ke stok. Stok sekarang: {self.stok} kg.")
    
    def informasi_buah(self):
        print(f"Nama Buah: {self.nama}")
        print(f"Harga per kg: ${self.harga_per_kg}")
        print(f"Stok: {self.stok} kg")
        print()

class TokoBuah:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_buah = []

    def tambah_buah(self, buah):
        self.daftar_buah.append(buah)
        print(f"{buah.nama} ditambahkan ke dalam toko {self.nama_toko}.")

    def cari_buah(self, nama):
        for buah in self.daftar_buah:
            if buah.nama.lower() == nama.lower():
                return buah
        return None

    def total_nilai_stok(self):
        total = 0
        for buah in self.daftar_buah:
            total += buah.harga_per_kg * buah.stok
        return total

    def tampilkan_daftar_buah(self):
        print(f"Daftar Buah di {self.nama_toko}:")
        if len(self.daftar_buah) == 0:
            print("Toko ini belum memiliki buah.")
        else:
            for buah in self.daftar_buah:
                buah.informasi_buah()

toko_buah = TokoBuah("Toko Buah Slamet")

nanas = Buah("Nanas", 10, 50)
alpukat = Buah("Alpukat", 15, 30)
kiwi = Buah("Kiwi", 8, 40)

toko_buah.tambah_buah(nanas)
toko_buah.tambah_buah(alpukat)
toko_buah.tambah_buah(kiwi)

toko_buah.tampilkan_daftar_buah()

nanas.update_harga(12)
kiwi.tambah_stok(20)

print("\nDaftar Buah Setelah Update:")
toko_buah.tampilkan_daftar_buah()

total_nilai = toko_buah.total_nilai_stok()
print(f"Total nilai stok buah di {toko_buah.nama_toko}: ${total_nilai}")
