class Mobil:
    def __init__(self, merk, model, tahun, warna):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.warna = warna
        self.kecepatan = 0

    def tambah_kecepatan(self, tambahan):
        self.kecepatan += tambahan
        print(f"Kecepatan {self.merk} {self.model} sekarang: {self.kecepatan} km/jam")

    def kurangi_kecepatan(self, pengurangan):
        self.kecepatan -= pengurangan
        print(f"Kecepatan {self.merk} {self.model} sekarang: {self.kecepatan} km/jam")

mobil1 = Mobil("Toyota", "Rush", 2024, "Putih")
mobil2 = Mobil("Honda", "Civic", 2020, "Putih")

mobil1.tambah_kecepatan(20)
mobil2.tambah_kecepatan(30)
mobil1.kurangi_kecepatan(10)
