# Looping List

semua_pengguna = ["Maman Supratman", "Aang Solihin", "Ferdiansyah Putra", "Jajang Priadi", "Mamat Nurohmat", "Vina Santika", "Delia Amanurin"]
semua_pengguna.sort()

# For loop
no = 1
for pengguna in semua_pengguna:
    print(f"Nama Pengguna Ke {no} Adalah {pengguna}")
    no += 1
    
print("")

# For loop dan range
panjang_list = len(semua_pengguna)
for index in range(panjang_list):
    print(f"Nama Pengguna Ke {index + 1} Adalah {semua_pengguna[index]}")
    
print("")

# While loop
index = 0
panjang_list = len(semua_pengguna)
while index < panjang_list:
    print(f"Nama Pengguna Ke {index + 1} Adalah {semua_pengguna[index]}")
    index += 1

# While loop dan range 
index = 0
panjang_list = len(semua_pengguna)
while index in range(panjang_list):
    print(f"Nama Pengguna Ke {index + 1} Adalah {semua_pengguna[index]}")
    index += 1

print("")

# List comprehension
no_pengguna = 1
[print(f"Nama Pengguna Adalah {pengguna}") for pengguna in semua_pengguna]

# Enumerate
for index, pengguna in enumerate(semua_pengguna):
    print(f"Nama Pengguna Ke {index + 1} Adalah {pengguna}")