# Function
# Function harus didefinisikan terlebih dahulu untuk bisa di panggil

# Function biasa
def showName(name):
    print(f"Nama Saya Adalah {name}")
    
showName("Aang Solihin")

# Function dengan return
def pertambahan(angka_pertama, angka_kedua):
    return angka_pertama + angka_kedua

angka_pertama = 10
angka_kedua = 20
hasil = pertambahan(angka_pertama, angka_kedua)

print(f"Hasil Dari Pertambahan Antara {angka_pertama} Dan {angka_kedua} Adalah {hasil}")

# Function dengan default argument
def sayHello(condition = "Datang", name = "Teman"):
    return f"Hallo Selamat {condition}, {name}."

print(sayHello())
print(sayHello(name="Aang Solihin"))
print(sayHello("Siang"))
