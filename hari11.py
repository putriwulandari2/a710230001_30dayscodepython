class Film:
    def __init__(self, judul, tahun_rilis, genre, durasi):
        self.judul = judul
        self.tahun_rilis = tahun_rilis
        self.genre = genre
        self.durasi = durasi
        self.rating = None

    def set_rating(self, rating):
        self.rating = rating

    def informasi(self):
        print(f"Informasi Film:\nJudul: {self.judul}\nTahun Rilis: {self.tahun_rilis}\nGenre: {self.genre}\nDurasi: {self.durasi} menit\nRating: {self.rating if self.rating else 'Belum dinilai'}")

film1 = Film("Ipar Adalah Maut", 2024, "Drama", 131)
film2 = Film("Agak Laen", 2024, "Komedi", 119)

film1.set_rating(9.3)
film2.set_rating(9.8)

film1.informasi()
film2.informasi()
