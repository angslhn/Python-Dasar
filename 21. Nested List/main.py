# Nested List

semua_pengguna = [["Maman Supratman", 23], ["Dani Ferdiansyah", 21], ["Dena Arumi", 22], ["Hidan Firmansyah", 24], ["Aang Solihin", 19]]
semua_pengguna.sort()

no = 1
for pengguna in semua_pengguna:
    print(f"Pengguna Ke {no}")
    print(f"Nama = {pengguna[0]}")
    print(f"Umur = {pengguna[1]}")
    print("")
    no += 1