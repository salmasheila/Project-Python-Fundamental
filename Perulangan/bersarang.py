# Input tinggi segitiga dari pengguna
tinggi = int(input("Masukkan tinggi segitiga: "))

# Loop bersarang untuk membuat pola segitiga siku-siku
for i in range(tinggi):
    for j in range(i + 1):
        print("*", end=" ")
    print()
