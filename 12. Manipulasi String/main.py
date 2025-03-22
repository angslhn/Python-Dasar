# Manipulasi String

# 1. Concatenation
nama_depan = "Aang"
nama_belakang = "Solihin"

nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari", nama_lengkap, "Adalah", panjang)

# 3. Operator untuk string
# Mengecek apa ada sebuah char atau string tertentu di dalam string
search = "Aa"
is_exist = search.lower() in nama_lengkap.lower()
print("Apakah", search, "ditemukan di", nama_lengkap, "?", is_exist)

search = "Maman"
is_not_exist = search.lower() not in nama_lengkap.lower()
print("Apakah", search, "tidak ditemukan di", nama_lengkap, "?", is_not_exist)

# Mengulang string
print(8*"—"*8)
print("Nama lengkap saya adalah", nama_lengkap)
print(8*"—"*8)

# Indexing string
huruf_pertama = nama_lengkap[0] 
huruf_terakhir = nama_lengkap[len(nama_lengkap) - 1] # Bisa juga dengan -1 dan seterusnya untuk mengambil index terakhir
print(nama_lengkap, "huruf pertama adalah", huruf_pertama, "dan huruf terakhir adalah", huruf_terakhir)

# Mengambil char dari index hingga index tertentu
nama_depan = nama_lengkap[0:nama_lengkap.index(" ")]
nama_belakang = nama_lengkap[(nama_lengkap.index(" ") + 1):len(nama_lengkap)]
print("Nama Depan =", nama_depan)
print("Nama Belakang =", nama_belakang)

# Item paling besar dan kecil pada string
big = max(nama_lengkap)
small = min(nama_lengkap)
print("Item paling besar dari", nama_lengkap, "adalah", big, "dan yang paling kecil adalah", small)

# ASCII Code
ascii_unicode = ord("A")
print("Kode unicode", ascii_unicode, "merupakan character", chr(ascii_unicode))