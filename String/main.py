# String

## Membuat String ##

# 1. Single quote
print('Hallo nama saya adalah Aang Solihin.')

# 2. Double quote
print("Saya berasal dari Sumedang.")

# Menggabungkan dua tipe quote
# Single quote didalam double quote 
print("Setiap hari jum'at saya akan pergi untuk juma'atan di masjid terdekat.")

# Double quote didalam single quote
print('"Hal paling sulit didunia ini adalah disiplin dan konsisten."')

## Penggunaan simbol \ ##

# 1. Mengubah tanda quote didalam quote menjadi string
print('Hari jum\'at adalah hari terakhir saya kuliah setaip 3 hari dalam seminggu.')

# 2. Mengubah tanda \ menjadi string
print('C:\GitHub\\new folder')

# 3. Menambahkan sebuah Tab
print("\tTeman saya bernama Maman Supratman.")

# 4. Menambahkan Backspace
print("Maman Supratman  \bumurnya adalah 21 tahun.")

# 5. Menambahkan baris baru
print("Ini adalah baris pertama.\nIni adalah baris kedua.\nIni adalah baris ketiga.")

## String literal dan raw

# 1. Raw
print(r"C:\new folder\new folder")

# 2. Multiline literal
print("""
\tNama : Aang Solihin
\tUmur : 19
\tHobi : Mendengarkan musik, Coding, dan Bermain Game Santai
""")

# 3. Multiline literal raw
print(r"""
\tNama : Maman Supratman
\tUmur : 21
\tHobi : Memancing, Menanam Pohon dan Mendaki Gunung
""")

# 4. Formatted string literal
a = 5
b = 10
print(f"Angka {a} ditambah angka {b} hasilnya adalah {a + b}")