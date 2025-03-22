# Format string

name = "Alice"
age = 25
height = 165.5

# Penggunaan dasar f-string
print(f"Nama: {name}, Umur: {age}, Tinggi: {height:.1f} cm")

# Justifikasi teks
print(f"{'Python':<10} | {'Belajar':^10} | {'Format':>10}")

# Menampilkan angka dalam berbagai format
num = 255
print(f"Biner: {num:b}, Oktal: {num:o}, Hexa: {num:X}, Desimal: {num:d}")

# Format angka dengan pemisah ribuan
large_num = 1234567890
print(f"Angka besar: {large_num:,}")

# Format dengan leading zeros
print(f"Nomor: {age:03d}")

# Format presisi angka float
pi = 3.14159265359
print(f"PI: {pi:.2f}")

# Menampilkan persentase
score = 0.875
print(f"Skor: {score:.1%}")

# Mengubah huruf besar/kecil
text = "python"
print(f"Upper: {text.upper()}, Lower: {text.lower()}")

# Menyisipkan karakter dalam string
symbol = "*"
print(f"{symbol:*^10}")

# Ekspresi dalam f-string
x, y = 10, 20
print(f"Hasil dari {x} + {y} = {x + y}")

# Penggunaan dalam kondisi logika
status = 'lulus' if age >= 18 else 'belum lulus'
print(f"Status: {status}")

# Mengakses elemen dalam list atau dictionary
data = {'nama': 'Alice', 'usia': 25}
print(f"Nama: {data['nama']}, Usia: {data['usia']}")

# Menentukan format waktu dan tanggal
from datetime import datetime
now = datetime.now()
print(f"Tanggal: {now:%Y-%m-%d}, Waktu: {now:%H:%M:%S}")

# Escape karakter dalam f-string
print(f"Harga: \${large_num:.2f}")
