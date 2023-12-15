class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_informasi(self):
        """Menampilkan informasi tentang buku."""
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print()

# Input informasi buku dari pengguna
judul_buku = input("Masukkan judul buku: ")
penulis_buku = input("Masukkan nama penulis: ")
tahun_terbit_buku = int(input("Masukkan tahun terbit buku: "))

# Membuat objek buku menggunakan kelas Buku
buku1 = Buku(judul_buku, penulis_buku, tahun_terbit_buku)

# Menampilkan informasi buku
print("Informasi Buku:")
buku1.tampilkan_informasi()

# Input informasi buku lainnya
judul_buku2 = input("Masukkan judul buku lain: ")
penulis_buku2 = input("Masukkan nama penulis buku lain: ")
tahun_terbit_buku2 = int(input("Masukkan tahun terbit buku lain: "))

# Membuat objek buku lainnya menggunakan kelas Buku
buku2 = Buku(judul_buku2, penulis_buku2, tahun_terbit_buku2)

# Menampilkan informasi buku lainnya
print("Informasi Buku Lain:")
buku2.tampilkan_informasi()
