inventory = {}

def tambah_produk(id_produk, nama_produk, harga, stok):
    if id_produk not in inventory:
        inventory[id_produk] = {'nama': nama_produk, 'harga': harga, 'stok': stok}
        print(f"Produk {nama_produk} berhasil ditambahkan ke inventaris.")
    else:
        print(f"Produk dengan ID {id_produk} sudah ada dalam inventaris.")

def hapus_produk(id_produk):
    if id_produk in inventory:
        del inventory[id_produk]
        print(f"Produk dengan ID {id_produk} berhasil dihapus dari inventaris.")
    else:
        print(f"Tidak ada produk dengan ID {id_produk} dalam inventaris.")

def tampilkan_informasi_produk(id_produk):
    if id_produk in inventory:
        produk = inventory[id_produk]
        print(f"Informasi Produk (ID: {id_produk}):")
        print(f"Nama: {produk['nama']}")
        print(f"Harga: {produk['harga']}")
        print(f"Stok: {produk['stok']}")
    else:
        print(f"Tidak ada produk dengan ID {id_produk} dalam inventaris.")

def update_stok(id_produk, jumlah):
    if id_produk in inventory:
        inventory[id_produk]['stok'] += jumlah
        print(f"Stok produk dengan ID {id_produk} berhasil diperbarui.")
    else:
        print(f"Tidak ada produk dengan ID {id_produk} dalam inventaris.")


# Tambahkan produk
tambah_produk(101, 'Pensil', 1.5, 50)
tambah_produk(102, 'Buku', 5.0, 30)

# Tampilkan informasi produk
tampilkan_informasi_produk(101)

# Update stok produk
update_stok(101, 20)

# Hapus produk
hapus_produk(102)
