class Mahasiswa:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
        self.nilai = []  

    def tambah_nilai(self, nilai):
        self.nilai.append(nilai)

    def rata_rata_nilai(self):
        if len(self.nilai) == 0:
            return 0
        return sum(self.nilai) / len(self.nilai)

    def info_mahasiswa(self):
        print(f"Nama: {self.nama}")
        print(f"Usia: {self.usia}")
        print(f"Nilai: {self.nilai}")
        print(f"Rata-rata Nilai: {self.rata_rata_nilai()}")


mahasiswa1 = Mahasiswa("Sukma Nur Safitri", 21)
mahasiswa2 = Mahasiswa("Allifah Septiani Putri", 20)

mahasiswa1.tambah_nilai(85)
mahasiswa1.tambah_nilai(75)
mahasiswa2.tambah_nilai(90)
mahasiswa2.tambah_nilai(80)

print("Informasi Mahasiswa 1:")
mahasiswa1.info_mahasiswa()

print("\nInformasi Mahasiswa 2:")
mahasiswa2.info_mahasiswa()
