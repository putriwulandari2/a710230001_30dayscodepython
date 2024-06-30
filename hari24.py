class Hewan:
    def __init__(self, nama, spesies, umur):
        self.nama = nama
        self.spesies = spesies
        self.umur = umur
    
    def __str__(self):
        return f"Nama: {self.nama}, Spesies: {self.spesies}, Umur: {self.umur} tahun"

class Kandang:
    def __init__(self, nama):
        self.nama = nama
        self.hewan = []
    
    def tambah_hewan(self, hewan):
        self.hewan.append(hewan)
        print(f"Hewan {hewan.nama} berhasil ditambahkan ke kandang {self.nama}.")
    
    def tampilkan_hewan(self):
        print(f"Daftar Hewan di Kandang {self.nama}:")
        for hewan in self.hewan:
            print(hewan)

class KebunBinatang:
    def __init__(self, nama):
        self.nama = nama
        self.kandang = []
    
    def tambah_kandang(self, kandang):
        self.kandang.append(kandang)
        print(f"Kandang {kandang.nama} berhasil ditambahkan ke kebun binatang {self.nama}.")
    
    def tampilkan_kandang(self):
        print(f"Daftar Kandang di Kebun Binatang {self.nama}:")
        for kandang in self.kandang:
            print(f"Kandang: {kandang.nama}")
            kandang.tampilkan_hewan()

kebun_binatang = KebunBinatang("Kebun Binatang Solo Safari")

kandang1 = Kandang("Karnivora")
kandang2 = Kandang("Herbivora")
kebun_binatang.tambah_kandang(kandang1)
kebun_binatang.tambah_kandang(kandang2)

hewan1 = Hewan("Simba", "Singa", 5)
hewan2 = Hewan("Slamet", "Harimau", 3)
hewan3 = Hewan("Bubu", "Rusa", 2)
hewan4 = Hewan("Gembrot", "Gajah", 6)

kandang1.tambah_hewan(hewan1)
kandang1.tambah_hewan(hewan2)
kandang2.tambah_hewan(hewan3)
kandang2.tambah_hewan(hewan4)

kebun_binatang.tampilkan_kandang()
