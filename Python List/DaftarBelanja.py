def tampilkan_daftar_belanja(daftar_belanja):
    print("\nDaftar Belanja:")
    for indeks, item in enumerate(daftar_belanja, start=1):
        print(f"{indeks}. {item}")

def tambah_item(daftar_belanja):
    item_baru = input("Masukkan item baru: ")
    daftar_belanja.append(item_baru)
    print(f"{item_baru} ditambahkan ke daftar belanja.")

def hapus_item(daftar_belanja):
    if not daftar_belanja:
        print("Daftar belanja kosong.")
        return

    tampilkan_daftar_belanja(daftar_belanja)
    indeks_hapus = int(input("Masukkan nomor item yang akan dihapus: "))

    if 1 <= indeks_hapus <= len(daftar_belanja):
        item_hapus = daftar_belanja.pop(indeks_hapus - 1)
        print(f"{item_hapus} dihapus dari daftar belanja.")
    else:
        print("Nomor item tidak valid.")

def main():
    daftar_belanja = []

    while True:
        print("\nMenu:")
        print("1. Tampilkan Daftar Belanja")
        print("2. Tambah Item ke Daftar Belanja")
        print("3. Hapus Item dari Daftar Belanja")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            tampilkan_daftar_belanja(daftar_belanja)
        elif pilihan == "2":
            tambah_item(daftar_belanja)
        elif pilihan == "3":
            hapus_item(daftar_belanja)
        elif pilihan == "4":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
