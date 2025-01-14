# Operator bitwise

a = 10
b = 5

# OR ( | )
hasil = a | b
print("\n Nilai a binary adalah", format(a, "08b"))
print(" Nilai b binary adalah", format(b, "08b"))
print(" Nilai a =", a, "dan nilai b =", b, "hasilnya adalah", hasil)

# AND ( & )
hasil = a & b
print("\n Nilai a binary adalah", format(a, "08b"))
print(" Nilai b binary adalah", format(b, "08b"))
print(" Nilai a =", a, "dan nilai b =", b, "hasilnya adalah", hasil)

# XOR ( ^ )
hasil = a ^ b
print("\n Nilai a binary adalah", format(a, "08b"))
print(" Nilai b binary adalah", format(b, "08b"))
print(" Nilai a =", a, "dan nilai b =", b, "hasilnya adalah", hasil)

# NOT ( ~ )
hasil = ~a
print("\n Nilai a binary adalah", format(a, "08b"))
print(" Nilai a =", a, "hasilnya adalah", hasil)

# Shift Right
# Menggeser angka biner ke kanan sebanyak angka yang di tuju
hasil = a >> 1
print("\n Nilai a binary adalah", format(a, "08b"))
print(" Nilai a =", a, "hasilnya adalah", hasil)

# Shift Left
# Menggeser angka biner ke kiri sebanyak angka yang di tuju
hasil = a << 5
print("\n Nilai a binary adalah", format(a, "08b"))
print(" Nilai a =", a, "hasilnya adalah", hasil)