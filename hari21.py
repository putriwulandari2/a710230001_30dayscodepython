class HP:
    def __init__(self, merek, model, harga, stok):
        self.merek = merek
        self.model = model
        self.harga = harga
        self.stok = stok
    
    def __str__(self):
        return f"Merek: {self.merek}, Model: {self.model}, Harga: {self.harga}, Stok: {self.stok}"

class Toko:
    def __init__(self, nama):
        self.nama = nama
        self.hp_list = []
    
    def tambah_hp(self, hp):
        self.hp_list.append(hp)
        print(f"HP {hp.merek} {hp.model} berhasil ditambahkan ke toko {self.nama}.")
    
    def tampilkan_hp(self):
        print(f"Daftar HP di Toko {self.nama}:")
        for hp in self.hp_list:
            print(hp)
    
    def beli_hp(self, merek, model):
        for hp in self.hp_list:
            if hp.merek == merek and hp.model == model:
                if hp.stok > 0:
                    hp.stok -= 1
                    print(f"HP {merek} {model} berhasil dibeli. Stok tersisa: {hp.stok}")
                    return
                else:
                    print(f"Stok HP {merek} {model} habis.")
                    return
        print(f"HP {merek} {model} tidak ditemukan di toko {self.nama}.")

class ManajemenToko:
    def __init__(self, nama):
        self.toko = Toko(nama)
    
    def tambah_hp(self, merek, model, harga, stok):
        hp = HP(merek, model, harga, stok)
        self.toko.tambah_hp(hp)
    
    def tampilkan_hp(self):
        self.toko.tampilkan_hp()
    
    def beli_hp(self, merek, model):
        self.toko.beli_hp(merek, model)

manajemen_toko = ManajemenToko("Erafone")

manajemen_toko.tambah_hp("Samsung", "Galaxy S23", 15000000, 10)
manajemen_toko.tambah_hp("Apple", "iPhone 12", 15000000, 6)
manajemen_toko.tambah_hp("Xiaomi", "Mi 11", 9000000, 8)

manajemen_toko.tampilkan_hp()

manajemen_toko.beli_hp("Samsung", "Galaxy S23")
manajemen_toko.beli_hp("Apple", "iPhone 12")

manajemen_toko.tampilkan_hp()
