def konversi_celsius_ke_fahrenheit(celsius):
    """Mengonversi suhu dari Celsius ke Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def konversi_fahrenheit_ke_celsius(fahrenheit):
    """Mengonversi suhu dari Fahrenheit ke Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Input suhu dari pengguna
suhu_input = float(input("Masukkan suhu: "))
skala_input = input("Masukkan skala suhu (C untuk Celsius, F untuk Fahrenheit): ")

# Lakukan konversi sesuai dengan skala input
if skala_input.upper() == 'C':
    suhu_fahrenheit = konversi_celsius_ke_fahrenheit(suhu_input)
    print(f"{suhu_input} derajat Celsius setara dengan {suhu_fahrenheit:.2f} derajat Fahrenheit.")
elif skala_input.upper() == 'F':
    suhu_celsius = konversi_fahrenheit_ke_celsius(suhu_input)
    print(f"{suhu_input} derajat Fahrenheit setara dengan {suhu_celsius:.2f} derajat Celsius.")
else:
    print("Skala suhu tidak valid. Harap masukkan C atau F.")
