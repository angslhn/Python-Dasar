# Method pada string

# lower
# Mengubah semua huruf menjadi huruf kecil
judul_buku = "The Great Gatsby"
print(judul_buku.lower())

# upper
# Mengubah semua huruf menjadi huruf besar
judul_film = "Avengers: Endgame"
print(judul_film.upper())

# title
# Mengubah huruf pertama setiap kata menjadi kapital
nama_produk = "samsung galaxy s24 ultra"
print(nama_produk.title())

# capitalize
# Mengubah huruf pertama menjadi kapital dan sisanya kecil
pesan = "halo, selamat datang di toko kami!"
print(pesan.capitalize())

# strip
# Menghapus spasi di awal dan akhir string
username = "   user123   "
print(username.strip())

# replace
# Mengganti substring tertentu dalam string
quote = "Belajar itu sulit tapi menyenangkan."
print(quote.replace("sulit", "mudah"))

# split
# Memecah string berdasarkan pemisah tertentu
hobi = "berenang, membaca, bermain game"
print(hobi.split(", "))

# join
# Menggabungkan elemen list menjadi string dengan pemisah tertentu
makanan_favorit = ["Pizza", "Burger", "Sushi"]
print(", ".join(makanan_favorit))

# find
# Mencari posisi substring dalam string, mengembalikan -1 jika tidak ditemukan
lirik = "Never gonna give you up"
print(lirik.find("give"))

# count
# Menghitung jumlah kemunculan substring dalam string
ulasan = "Bagus banget! Tempatnya bagus, makanannya juga bagus."
print(ulasan.count("bagus"))

# startswith
# Mengecek apakah string dimulai dengan substring tertentu
website = "https://google.com"
print(website.startswith("https"))

# endswith
# Mengecek apakah string diakhiri dengan substring tertentu
file_name = "document.pdf"
print(file_name.endswith(".pdf"))

# isdigit
# Mengecek apakah semua karakter dalam string adalah angka
kode_pos = "40123"
print(kode_pos.isdigit())

# isalpha
# Mengecek apakah semua karakter dalam string adalah huruf
nama_depan = "Jonathan"
print(nama_depan.isalpha())

# isalnum
# Mengecek apakah semua karakter dalam string adalah huruf atau angka
kode_kupon = "DISKON50"
print(kode_kupon.isalnum())

# swapcase
# Menukar huruf besar menjadi kecil dan sebaliknya
status = "Python is FUN!"
print(status.swapcase())

# zfill
# Menambahkan nol di depan string hingga panjang tertentu
nomor_antrian = "25"
print(nomor_antrian.zfill(5))

# center
# Meletakkan teks di tengah dengan padding tertentu
judul = "Promo Besar-Besaran"
print(judul.center(30, "*"))

# ljust
# Meratakan teks ke kiri dengan lebar tertentu
produk = "Laptop"
print(produk.ljust(15, "."))

# rjust
# Meratakan teks ke kanan dengan lebar tertentu
harga = "Rp 1.500.000"
print(harga.rjust(20, "."))

# partition
# Memisahkan string menjadi tiga bagian berdasarkan substring pertama yang ditemukan
email = "user@gmail.com"
print(email.partition("@"))

# maketrans dan translate
# Mengganti karakter dalam string dengan tabel translasi
tabel_translasi = str.maketrans("aeiou", "12345")
kalimat = "Selamat Pagi Dunia"
print(kalimat.translate(tabel_translasi))

# casefold
# Mengubah semua huruf menjadi huruf kecil (lebih agresif dari lower)
bahasa = "Straße"
print(bahasa.casefold())

# expandtabs
# Mengubah tab dalam string menjadi spasi dengan panjang tertentu
kalimat = "Nama\tUsia\tKota"
print(kalimat.expandtabs(10))