class Pegawai:
    def __init__(self, nama, id_pegawai, jabatan, gaji):
        self.nama = nama
        self.id_pegawai = id_pegawai
        self.jabatan = jabatan
        self.gaji = gaji

    def informasi(self):
        print(f"Informasi Pegawai:\nNama: {self.nama}\nID Pegawai: {self.id_pegawai}\nJabatan: {self.jabatan}\nGaji: Rp{self.gaji}")

    def naik_gaji(self, persen_kenaikan):
        kenaikan = self.gaji * (persen_kenaikan / 100)
        self.gaji += kenaikan
        print(f"Gaji {self.nama} naik sebesar {persen_kenaikan}%. Gaji sekarang: Rp{self.gaji}")

    def ganti_jabatan(self, jabatan_baru):
        self.jabatan = jabatan_baru
        print(f"Jabatan {self.nama} sekarang: {self.jabatan}")

pegawai1 = Pegawai("Abdul", "022", "Manager", 25000000)
pegawai2 = Pegawai("Dani", "002", "Staff", 8000000)

pegawai1.informasi()
pegawai2.informasi()

pegawai1.naik_gaji(10)  
pegawai2.ganti_jabatan("Supervisor")
