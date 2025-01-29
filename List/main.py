# List

# List numbers
angka = [i for i in range(1, 10)]
print(f"Isi dari list angka adalah {angka}")

# List string
semua_pengguna = ["Maman", "Deden", "Supardi", "Zidan", "Doni", "Mamat", "Beni"]
index = 1
for pengguna in semua_pengguna:
    print(f"Pengguna ke {index} adalah {pengguna}")
    index += 1

# List campuran
semua_pengguna = ["Maman", 21, "Deden", 23, "Supardi", 25, "Zidan", 22, "Doni", 24, "Mamat", 27, "Beni", 29]

no = 1
index_pengguna = 0
index_umur = 1
for index in range(int((len(semua_pengguna) / 2))):
    
    print(f"Pengguna ke {no} adalah {semua_pengguna[index_pengguna]} berumur {semua_pengguna[index_umur]}")
    
    no += 1
    index_pengguna += 2
    index_umur += 2
