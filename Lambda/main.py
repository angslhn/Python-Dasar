# Lambda
# Cara membuat function cukup singkat
# <variable> = lambda <parameter>: <tugas>

# Dengan variable
tampilkan_informasi = lambda nama, umur: print(f"Nama {nama} dan umur {umur}")
tampilkan_informasi(nama="Aang Solihin", umur=17)

# Digunakan sebagai argument
angka = [1, 6, 8, 3, 7, 4, 9, 5, 2, 10, 15, 13, 14, 12, 11]

angka_genap = list(filter(lambda angka: angka % 2 == 0, angka))
angka_genap.sort()
print(angka_genap)

angka_ganjil = list(filter(lambda angka: angka % 2 == 1, angka))
angka_ganjil.sort()
print(angka_ganjil)

# Anonymous function
def pangkat(angka):
    return lambda n: angka ** n

print(f"{pangkat(5)(2)}")