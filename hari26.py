class Kendaraan:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0
        self.engine_status = False

    def nyalakan_mesin(self):
        if not self.engine_status:
            self.engine_status = True
            print(f"Mesin {self.merek} {self.model} telah dinyalakan.")
        else:
            print(f"Mesin {self.merek} {self.model} sudah menyala.")

    def matikan_mesin(self):
        if self.engine_status:
            self.engine_status = False
            self.kecepatan = 0
            print(f"Mesin {self.merek} {self.model} telah dimatikan.")
        else:
            print(f"Mesin {self.merek} {self.model} sudah mati.")

    def percepat(self, jumlah):
        if self.engine_status:
            self.kecepatan += jumlah
            print(f"{self.merek} {self.model} melaju dengan kecepatan {self.kecepatan} km/jam.")
        else:
            print(f"Nyalakan mesin {self.merek} {self.model} terlebih dahulu.")

    def rem(self):
        if self.kecepatan > 0:
            self.kecepatan = max(0, self.kecepatan - 10)
            print(f"{self.merek} {self.model} melambat. Kecepatan saat ini {self.kecepatan} km/jam.")
        else:
            print(f"{self.merek} {self.model} sudah berhenti.")

    def tampilkan_info(self):
        print(f"Merek: {self.merek}, Model: {self.model}, Tahun: {self.tahun}")
        print(f"Status Mesin: {'Menyala' if self.engine_status else 'Matikan'}, Kecepatan Saat Ini: {self.kecepatan} km/jam")


mobil1 = Kendaraan("Toyota", "Camry", 2020)
mobil2 = Kendaraan("Honda", "Civic", 2021)

mobil1.nyalakan_mesin()

mobil2.nyalakan_mesin()
mobil2.percepat(50)
mobil2.rem()

print("\nInformasi Mobil Pertama:")
mobil1.tampilkan_info()

print("\nInformasi Mobil Kedua:")
mobil2.tampilkan_info()
