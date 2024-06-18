class Mahasiswa:
    def __init__(self, nama, nim, jurusan, tahun_masuk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.tahun_masuk = tahun_masuk
        self.ipk = 0.0
        self.jumlah_sks = 0

    def ambil_mata_kuliah(self, jumlah_sks, nilai):
        self.jumlah_sks += jumlah_sks
        total_nilai = self.ipk * (self.jumlah_sks - jumlah_sks)
        total_nilai += nilai * jumlah_sks
        self.ipk = total_nilai / self.jumlah_sks

    def informasi(self):
        print(f"Informasi Mahasiswa:\nNama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}\nTahun Masuk: {self.tahun_masuk}\nIPK: {self.ipk:.2f}\nJumlah SKS: {self.jumlah_sks}")

mahasiswa1 = Mahasiswa("Zaki", "A710210034", "Informatika", 2021)
mahasiswa2 = Mahasiswa("Ainun", "A420230001", "Biologi", 2021)

mahasiswa1.ambil_mata_kuliah(3, 4.0)  
mahasiswa1.ambil_mata_kuliah(4, 3.5)  

mahasiswa2.ambil_mata_kuliah(2, 3.0) 
mahasiswa2.ambil_mata_kuliah(3, 3.7)  

mahasiswa1.informasi()
mahasiswa2.informasi()
