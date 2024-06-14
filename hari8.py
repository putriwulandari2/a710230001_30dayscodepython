class Restoran:
    def __init__(self, nama, jenis_masakan, rating):
        self.nama = nama
        self.jenis_masakan = jenis_masakan
        self.rating = rating
        self.jumlah_pelanggan = 0

    def informasi(self):
        print(f"Informasi Restoran:\nNama: {self.nama}\nJenis Masakan: {self.jenis_masakan}\nRating: {self.rating}\nJumlah Pelanggan: {self.jumlah_pelanggan}")

    def tambah_pelanggan(self, jumlah):
        self.jumlah_pelanggan += jumlah
        print(f"Jumlah pelanggan di {self.nama} sekarang: {self.jumlah_pelanggan}")

restoran1 = Restoran("Marugame Udon", "Masakan Japan", 4.9)
restoran2 = Restoran("Pizza Hut", "Masakan Italia", 4.5)

restoran1.informasi()
restoran2.informasi()

restoran1.tambah_pelanggan(10)
