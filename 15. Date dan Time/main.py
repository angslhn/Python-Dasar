#  Datetime

# Format kode penting:
# %d - Hari (01-31)
# %m - Bulan (01-12)
# %Y - Tahun (4 digit)
# %y - Tahun (2 digit)
# %H - Jam (00-23)
# %I - Jam (01-12, format 12 jam)
# %p - AM/PM
# %M - Menit (00-59)
# %S - Detik (00-59)
# %A - Nama hari penuh
# %a - Nama hari singkat
# %B - Nama bulan penuh
# %b - Nama bulan singkat
# %w - Hari dalam minggu (0=Minggu, 6=Sabtu)

## 1. Import Module
from datetime import datetime, date, time, timedelta

## 2. Mendapatkan Tanggal dan Waktu Sekarang
# Tanggal dan waktu sekarang
now = datetime.now()
print(now)  # Output: 2025-01-24 14:30:00.123456

# Hanya tanggal hari ini
today = date.today()
print(today)  # Output: 2025-01-24

## 3. Format Tanggal dan Waktu
# Format ke string
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_date)  # Output: 24-01-2025 14:30:00

## 4. Parsing String ke Tanggal
date_str = "24-01-2025 14:30:00"
parsed_date = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print(parsed_date)  # Output: 2025-01-24 14:30:00

## 5. Mendapatkan Komponen Tanggal dan Waktu
print(now.year)  # Output: 2025
print(now.month)  # Output: 1
print(now.day)  # Output: 24
print(now.hour)  # Output: 14
print(now.minute)  # Output: 30
print(now.second)  # Output: 0
print(now.weekday())  # Output: 4 (Senin=0, Minggu=6)
print(now.isoweekday())  # Output: 5 (Senin=1, Minggu=7)

## 6. Perhitungan Tanggal dan Waktu
# Tambah atau kurang waktu
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)

print(tomorrow)  # Output: 2025-01-25
print(yesterday)  # Output: 2025-01-23

# Selisih dua tanggal
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 1, 24)
difference = end_date - start_date
print(difference.days)  # Output: 23 hari

## 7. Timezone (Zona Waktu)
import pytz

# Mendapatkan waktu dalam zona tertentu
utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
jakarta_tz = pytz.timezone('Asia/Jakarta')
jakarta_time = utc_now.astimezone(jakarta_tz)

print(jakarta_time)  # Output: 2025-01-24 21:30:00+07:00

## 8. Membuat Objek Tanggal dan Waktu
custom_date = datetime(2025, 1, 24, 14, 30, 0)
print(custom_date)  # Output: 2025-01-24 14:30:00

## 9. Cek Leap Year (Tahun Kabisat)
import calendar

year = 2024
print(calendar.isleap(year))  # Output: True

## 10. Menghitung Minggu dan Bulan dengan Index 0
week_day = now.weekday()  # Senin = 0, Minggu = 6
month_index = now.month - 1  # Januari = 0, Desember = 11

print(week_day)  # Output: 4 (misalnya untuk Jumat)
print(month_index)  # Output: 0 (untuk Januari)

## 11. Konversi Timestamp ke Datetime
timestamp = 1706052600
converted_date = datetime.fromtimestamp(timestamp)
print(converted_date)  # Output: 2025-01-24 14:30:00

## 12. Konversi Datetime ke Timestamp
timestamp_value = now.timestamp()
print(timestamp_value)  # Output: 1706052600.0

## 13. Waktu Default dalam Python
# Waktu default untuk perbandingan
print(datetime.min)  # Output: 0001-01-01 00:00:00
print(datetime.max)  # Output: 9999-12-31 23:59:59.999999