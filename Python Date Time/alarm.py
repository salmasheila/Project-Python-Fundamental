from datetime import datetime
from playsound import playsound

# Mendapatkan waktu saat ini
sekarang = datetime.now()

# Menampilkan waktu saat ini
print(sekarang)

# Meminta pengguna untuk memasukkan waktu alarm
alarm_time = input("Masukkan waktu alarm (HH:MM:SS): ")

# Memisahkan jam, menit, dan detik dari waktu yang dimasukkan
alarm_hour, alarm_minute, alarm_seconds = map(int, alarm_time.split(':'))

print("Mengatur alarm...")

# Loop utama untuk memeriksa alarm
while True:
    now = datetime.now()
    
    # Mendapatkan jam, menit, dan detik saat ini
    current_hour = now.hour
    current_minute = now.minute
    current_seconds = now.second

    # Memeriksa apakah waktu alarm telah tercapai
    if alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds:
        print("Bangun!")
        
        # Memutar suara alarm (pastikan file 'alarm.mp3' ada di direktori yang benar)
        # playsound('alarm.mp3')

        break
