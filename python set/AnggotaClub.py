# insiasi set
anggota_klub = set()

#tambah anggota
def tambah_anggota(nama_anggota):
    anggota_klub.add(nama_anggota)
    print(f"{nama_anggota} berhasil ditambahkan sebagai anggota klub.")

# Hapus Anggota
def hapus_anggota(nama_anggota):
    if nama_anggota in anggota_klub:
        anggota_klub.remove(nama_anggota)
        print(f"{nama_anggota} berhasil dihapus dari anggota klub.")
    else:
        print(f"{nama_anggota} tidak ditemukan dalam anggota klub.")

#Tampilkan daftar Anggota
def tampilkan_anggota():
    print("Daftar Anggota Klub:")
    for anggota in anggota_klub:
        print(anggota)


# Tambahkan anggota baru
tambah_anggota("Alice")
tambah_anggota("Bob")
tambah_anggota("Charlie")

# Tampilkan daftar anggota
tampilkan_anggota()

# Hapus anggota
hapus_anggota("Bob")

# Tampilkan daftar anggota setelah penghapusan
tampilkan_anggota()
