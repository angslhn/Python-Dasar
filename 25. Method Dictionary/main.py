# Method Dictionary

users = [
    {
        "username" : "angslhn",
        "fullname" : "Aang Solihin",
        "email" : "angslhn@gmail.com",
        "password" : "aangsolihincoolbet"
    },
    {
        "username" : "mamansupratman",
        "fullname" : "Maman Supratman",
        "email" : "mamansupratman@gmail.com",
        "password" : "mamanganteng100%"
    },
    {
        "username" : "Dedi Supardi",
        "fullname" : "dedisupardi",
        "email" : "dedisupardi@gmail.com",
        "password" : "dedisupardisangatlahtampan"
    },
    {
        "username" : "mamatrahmat",
        "fullname" : "Mamat Rahmat",
        "email" : "mamatrahmat@gmail.com",
        "password" : "mamatsuperganteng"
    }
]

# keys
# Mengembalikan semua kunci dalam dictionary.
print(users[0].keys())

# values
# Mengembalikan semua nilai dalam dictionary.
print(users[0].values())

# items
# Mengembalikan semua pasangan key-value sebagai tuple dalam list.
print(users[0].items())

# get
# Mengambil nilai berdasarkan kunci, mengembalikan none jika tidak ditemukan.
print(users[0].get("username"))
print(users[0].get("nama", "Tidak Ditemukan"))

# update
# Memperbarui dictionary dengan pasangan key-value dari dictionary lain, jika tidak ada maka akan di tambahkan.
users[3].update({"username" : "jajangsupardi", "fullname" : "Jajang Supardi", "email" : "jajangsupardi@gmail.com", "password" : "jajangperkasadangagah"})
print(users[3].values())

# pop
# Menghapus item berdasarkan kunci, mengembalikan nilai item, atau default jika tidak ditemukan.
users[0].pop("username")
print(users[0].items())

# popitem
# Menghapus dan mengembalikan item terakhir sebagai tuple (key, value).
users[1].popitem()
print(users[1].items())

# setdefault
# Mengembalikan nilai dari key jika ada, atau menambahkan key dengan nilai default jika tidak ada.
users[0].setdefault("username", "angslhn")
users[1].setdefault("password", "mamanganteng100%")

print(users[0].items())
print(users[1].items())

# clear
# Menghapus semua item dalam dictionary.
users[3].clear()
print(users[3].items())