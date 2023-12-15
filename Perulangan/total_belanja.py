def hitung_total_belanja():
    """Menghitung total belanja dari beberapa item."""
    total_belanja = 0

    while True:
        nama_barang = input("Masukkan nama barang (atau ketik 'selesai' untuk mengakhiri): ")

        if nama_barang.lower() == 'selesai':
            break

        try:
            harga_barang = float(input("Masukkan harga barang: "))
            jumlah_barang = int(input("Masukkan jumlah barang: "))
            total_belanja += harga_barang * jumlah_barang
        except ValueError:
            print("Masukkan harga dan jumlah dalam format yang benar.\n")

    return total_belanja

# Program Utama
print("Selamat datang di Program Hitung Total Belanja")

total_belanja = hitung_total_belanja()

print(f"\nTotal belanja Anda adalah: ${total_belanja:.2f}")
print("Terima kasih telah menggunakan program kami!")
