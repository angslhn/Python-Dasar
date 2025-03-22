# with
# Keyword with di Python digunakan untuk memastikan bahwa file ditutup secara otomatis setelah digunakan

# open()
# Fungsi ini digunakan untuk membuka file dalam mode tertentu.

# Parameter	pada open()
# file	    --> Nama atau path file yang ingin dibuka (wajib).
# mode	    --> Menentukan mode operasi file (opsional, default: 'r').
#          'r'	Membaca file (error jika file tidak ada).
#          'w'	Menulis file (menghapus isi lama jika file sudah ada).
#          'a'	Menambahkan teks ke akhir file.
#          'x'	Membuat file baru (error jika sudah ada).
#          'rb' Membaca file dalam mode biner.
#          'wb'	Menulis file dalam mode biner.
#          'ab'	Menambahkan dalam mode biner.
#          'r+'	Membaca dan menulis (tidak menghapus isi lama).
#          'w+'	Membaca dan menulis (menghapus isi lama).
#          'a+'	Membaca dan menulis (menambahkan ke akhir file).
# buffering	--> Menentukan penggunaan buffering: 0 (tanpa buffering), 1 (buffering baris untuk file teks), >1 (ukuran buffer dalam byte), -1 (default sistem).
# encoding	--> Encoding file, misalnya 'utf-8', 'ascii', dll. Hanya berlaku untuk file teks.
# errors	--> Menentukan bagaimana kesalahan encoding/decoding ditangani (misalnya, 'ignore', 'replace', 'strict').
# newline	--> Menentukan bagaimana karakter newline (\n, \r\n, dll.) diperlakukan dalam mode teks.
# closefd	--> Jika False, file descriptor tidak akan ditutup saat objek file ditutup (hanya berlaku jika file adalah integer, bukan string).
# opener	--> Fungsi khusus untuk membuka file dengan cara yang ditentukan pengguna.

para_pengguna = ['Aang Solihin', 19, 'Maman Supratman', 23, 'Deden Ferdiansyah', 22]

with open(file='data_pengguna.txt', mode='a', encoding='utf-8') as file:
    for nama, umur in zip(para_pengguna[::2], para_pengguna[1::2]):
        file.write(f"Nama Pengguna = {nama}\nUmur = {umur}\n\n")
    