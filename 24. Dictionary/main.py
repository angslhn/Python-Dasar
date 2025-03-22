# Dictionary

semua_pengguna = [
    {
    "nama" : "Aang Solihin",
    "umur" : 19
    },
    {
    "nama" : "Beni Supardi",
    "umur" : 27
    },
    {
    "nama" : "Jajang Priyatna",
    "umur" : 22
    },
    {
    "nama" : "Mamat Rahmat",
    "umur" : 23
    }
]

for index, pengguna in enumerate(semua_pengguna, start=1):
    print(f"\nPengguna Ke {index}")
    print(f"Nama = {pengguna["nama"]}")
    print(f"Umur = {pengguna["umur"]}")