# Looping

# For loop
for index in range(5):
    print(f"No. {index + 1}")

semua_pengguna = ["Maman", "Nanang", "Deden", "Supardi", "Mamat", "Ahmad", "Gunawan"]

no = 1
for pengguna in semua_pengguna:
    print(f"Pengguna Ke {no} Adalah {pengguna}")
    no += 1
    
# While loop
angka = 1
while angka <= 10:
    print(f"No. {angka}")
    angka += 1