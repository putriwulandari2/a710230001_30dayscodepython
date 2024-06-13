class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, jumlah):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.jumlah = jumlah
        self.jumlah_tersedia = jumlah

    def pinjam(self):
        if self.jumlah_tersedia > 0:
            self.jumlah_tersedia -= 1
            return True
        else:
            return False

    def kembalikan(self):
        if self.jumlah_tersedia < self.jumlah:
            self.jumlah_tersedia += 1
            return True
        else:
            return False

class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def daftar_buku(self):
        if not self.koleksi_buku:
            print("Tidak ada buku di perpustakaan.")
        else:
            for buku in self.koleksi_buku:
                print(f"Judul: {buku.judul}, Pengarang: {buku.pengarang}, Tahun Terbit: {buku.tahun_terbit}, Tersedia: {buku.jumlah_tersedia}/{buku.jumlah}")

    def pinjam_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul == judul:
                if buku.pinjam():
                    print(f"Buku '{judul}' berhasil dipinjam.")
                else:
                    print(f"Buku '{judul}' tidak tersedia untuk dipinjam.")
                return
        print(f"Buku '{judul}' tidak ditemukan di perpustakaan.")

    def kembalikan_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul == judul:
                if buku.kembalikan():
                    print(f"Buku '{judul}' berhasil dikembalikan.")
                else:
                    print(f"Buku '{judul}' sudah dalam jumlah maksimal.")
                return
        print(f"Buku '{judul}' tidak ditemukan di perpustakaan.")

def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Daftar Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            tahun_terbit = input("Masukkan tahun terbit buku: ")
            jumlah = int(input("Masukkan jumlah buku: "))
            buku = Buku(judul, pengarang, tahun_terbit, jumlah)
            perpustakaan.tambah_buku(buku)
            print(f"Buku '{judul}' berhasil ditambahkan ke perpustakaan.")
        
        elif pilihan == '2':
            perpustakaan.daftar_buku()
        
        elif pilihan == '3':
            judul = input("Masukkan judul buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(judul)
        
        elif pilihan == '4':
            judul = input("Masukkan judul buku yang ingin dikembalikan: ")
            perpustakaan.kembalikan_buku(judul)
        
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi perpustakaan.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
