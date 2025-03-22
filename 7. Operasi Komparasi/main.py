# Operasi komparasi
a = 5
b = 7

# Lebih besar dari
hasil = a > b
print("\n", a, "lebih besar dari", b, "adalah", hasil)

# Lebih kecil dari
hasil = a < b
print("\n", a, "lebih kecil dari", b, "adalah", hasil)

# Lebih besar sama dengan
hasil = a >= b
print("\n", a, "lebih besar sama dengan", b, "adalah", hasil)

# Lebih kecil sama dengan
hasil = a <= b
print("\n",a, "lebih kecil sama dengan", b, "adalah", hasil)

# Sama dengan
hasil = a == b
print("\n", a, "Sama dengan", b, "adalah", hasil)

# Tidak sama dengan
hasil = a != b
print("\n", a, "Tidak sama dengan", b, "adalah", hasil)

# Komparasi object identity
x = 10
y = 10

print("\n", "Alamat memori dari nilai", x, "adalah", hex(id(x)))
print("\n", "Alamat memori dari nilai", y, "adalah", hex(id(y)))

hasil = x is y
print("\n", x, "Sama dengan", y, "adalah", hasil)

hasil = x is not y
print("\n", x, "Tidak sama dengan", y, "adalah", hasil)