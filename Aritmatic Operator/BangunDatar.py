import math

def hitung_luas_persegi(sisi):
    return sisi ** 2

def hitung_keliling_persegi(sisi):
    return 4 * sisi

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def hitung_luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

def hitung_keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def main():
    while True:
        print("\nKalkulator Luas dan Keliling")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Keluar")

        pilihan = input("Pilih bentuk (1/2/3/4): ")

        if pilihan == "4":
            print("Terima kasih! Keluar dari kalkulator.")
            break

        try:
            if pilihan in ["1", "2"]:
                sisi = float(input("Masukkan panjang sisi: "))
            elif pilihan == "3":
                jari_jari = float(input("Masukkan panjang jari-jari: "))
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                continue
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if pilihan == "1":
            luas = hitung_luas_persegi(sisi)
            keliling = hitung_keliling_persegi(sisi)
        elif pilihan == "2":
            lebar = float(input("Masukkan lebar sisi: "))
            luas = hitung_luas_persegi_panjang(sisi, lebar)
            keliling = hitung_keliling_persegi_panjang(sisi, lebar)
        elif pilihan == "3":
            luas = hitung_luas_lingkaran(jari_jari)
            keliling = hitung_keliling_lingkaran(jari_jari)

        print(f"Luas: {luas}")
        print(f"Keliling: {keliling}")

if __name__ == "__main__":
    main()
