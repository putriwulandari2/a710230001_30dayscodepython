class Kampus:
    def __init__(self):
        self.mahasiswa = {}
        self.dosen = {}
        self.mata_kuliah = {}
    
    def tambah_mahasiswa(self, nim, nama, jurusan):
        self.mahasiswa[nim] = {
            'nama': nama,
            'jurusan': jurusan
        }
        print(f"Mahasiswa {nama} berhasil ditambahkan.")
    
    def tambah_dosen(self, nip, nama, departemen):
        self.dosen[nip] = {
            'nama': nama,
            'departemen': departemen
        }
        print(f"Dosen {nama} berhasil ditambahkan.")
    
    def tambah_mata_kuliah(self, kode, nama_mk, sks):
        self.mata_kuliah[kode] = {
            'nama_mk': nama_mk,
            'sks': sks
        }
        print(f"Mata kuliah {nama_mk} berhasil ditambahkan.")
    
    def tampilkan_mahasiswa(self):
        print("Daftar Mahasiswa:")
        for nim, info in self.mahasiswa.items():
            print(f"NIM: {nim}, Nama: {info['nama']}, Jurusan: {info['jurusan']}")
    
    def tampilkan_dosen(self):
        print("Daftar Dosen:")
        for nip, info in self.dosen.items():
            print(f"NIP: {nip}, Nama: {info['nama']}, Departemen: {info['departemen']}")
    
    def tampilkan_mata_kuliah(self):
        print("Daftar Mata Kuliah:")
        for kode, info in self.mata_kuliah.items():
            print(f"Kode: {kode}, Nama: {info['nama_mk']}, SKS: {info['sks']}")

kampus = Kampus()

kampus.tambah_mahasiswa("A710190016", "Zaky Septian", "Pend Teknik Informatika")
kampus.tambah_mahasiswa("A420230001", "Ainun Marghiah", "Pend Geografi")

kampus.tambah_dosen("67890234", "Arif Setiawan,M.Eng", "Teknik Informatika")
kampus.tambah_dosen("67891546", "Dr. Puspita Indra Wardhani", "Pend Geografia")

kampus.tambah_mata_kuliah("INF101", "Pemrograman Berorientasi Objek", 3)
kampus.tambah_mata_kuliah("INF102", "Geografi Manusia", 4)

kampus.tampilkan_mahasiswa()
kampus.tampilkan_dosen()
kampus.tampilkan_mata_kuliah()
