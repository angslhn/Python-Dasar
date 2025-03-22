# Operasi Boolean

x = True
y = False

# NOT
# Kebalikan dari nilai di sebuah variable tersebut
hasil = not x
print("X =", x, "Adalah", hasil)

# OR
# Mengambil salah satunya jika ada yang bernilai True
hasil = x or y
print("X =", x, "Y =", y, "Adalah", hasil)

# AND
# Akan bernilai True, jika kedua atau lebih nilainya adalah True
hasil = x and y
print("X =", x, "Y =", y, "Adalah", hasil)

# XOR
# Akan bernilai True, jika salah satu nilainya adalah True
# Akan bernilai False, jika semua nilainya adalah sama
hasil = x ^ y
print("X =", x, "Y =", y, "Adalah", hasil)