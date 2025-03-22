# Manipulasi List
# Index pertama di mulai dengan 0

# Mengakses List
semua_nama = ["Aang Solihin", "Ahmad Fauzi", "Amri Hidayat", "Brian Putra Sihombing", "Cantika Putri", "Dea Hianuri"]
print(f"Nama ke 1 didalam list adalah {semua_nama[0]}")

# Mengubah isi List
kota = ["Sumedang", "Bandung", "Cimahi", "Bogor", "Garut", "Pangandaran", "Sukabumi", "Bekasi"]
kota[2] = "Banten"
print(kota[2])

### 1. Menambahkan Elemen ke List

# Append
# Menambahkan satu elemen ke akhir list
angka = [1, 2, 3]
angka.append(4)
print(angka)  # Output: [1, 2, 3, 4]

# Extend
# Menambahkan beberapa elemen (iterable) ke akhir list
angka = [1, 2, 3]
angka.extend([4, 5, 6])
print(angka)  # Output: [1, 2, 3, 4, 5, 6]

# Insert
# Menyisipkan elemen ke posisi tertentu dalam list
angka = [1, 2, 4]
angka.insert(2, 3)  # Menyisipkan angka 3 di indeks ke-2
print(angka)  # Output: [1, 2, 3, 4]

### 2. Menghapus Elemen dari List

# Remove
# Menghapus elemen pertama yang cocok dengan nilai yang diberikan
angka = [1, 2, 3, 2, 4]
angka.remove(2)  # Menghapus elemen pertama yang bernilai 2
print(angka)  # Output: [1, 3, 2, 4]

# Pop
# Menghapus dan mengembalikan elemen pada indeks tertentu (default terakhir)
angka = [1, 2, 3]
x = angka.pop()  # Menghapus elemen terakhir
print(angka)  # Output: [1, 2]
print(x)  # Output: 3

angka = [1, 2, 3]
y = angka.pop(1)  # Menghapus elemen indeks ke-1
print(angka)  # Output: [1, 3]
print(y)  # Output: 2

# Clear
# Menghapus semua elemen dalam list
angka = [1, 2, 3]
angka.clear()
print(angka)  # Output: []

### 3. Mencari Elemen dalam List

# Index
#Mengembalikan indeks pertama dari elemen yang sesuai
angka = [10, 20, 30, 40]
print(angka.index(30))  # Output: 2

# Count
# Mengembalikan jumlah kemunculan suatu elemen dalam list
angka = [1, 2, 2, 3, 2]
print(angka.count(2))  # Output: 3

### 4. Mengurutkan dan Membalik List

# Sort
# Mengurutkan elemen dalam list secara ascending atau descending
angka = [3, 1, 4, 1, 5, 9]
angka.sort()
print(angka)  # Output: [1, 1, 3, 4, 5, 9]

angka.sort(reverse=True)
print(angka)  # Output: [9, 5, 4, 3, 1, 1]

# Sorted
# Mengembalikan list baru yang sudah diurutkan tanpa mengubah list asli
angka = [3, 1, 4, 1, 5, 9]
new_angka = sorted(angka)
print(new_angka)  # Output: [1, 1, 3, 4, 5, 9]
print(angka)  # Output: [3, 1, 4, 1, 5, 9]

# Reverse
# Membalik urutan elemen dalam list
angka = [1, 2, 3, 4, 5]
angka.reverse()
print(angka)  # Output: [5, 4, 3, 2, 1]

### 5. Menyalin List

# Copy
# Membuat salinan baru dari list
angka = [1, 2, 3]
new_angka = angka.copy()
print(new_angka)  # Output: [1, 2, 3]

### 6. Operasi Lainnya

# len
# Mengembalikan jumlah elemen dalam list.
angka = [1, 2, 3, 4]
print(len(angka))  # Output: 4

# Operator + (Gabung List)
# Menggabungkan dua list menjadi satu.
angka1 = [1, 2, 3]
angka2 = [4, 5, 6]
result = angka1 + angka2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Operator * (Duplikasi List)
# Mengulangi elemen dalam list sebanyak n kali.
angka = [1, 2, 3]
print(angka * 2)  # Output: [1, 2, 3, 1, 2, 3]

# in dan not in
#Mengecek apakah elemen ada di dalam list.
angka = [1, 2, 3, 4]
print(2 in angka)  # Output: True
print(5 not in angka)  # Output: True

# List Comprehension (Membuat List Baru)
# Membuat list berdasarkan kondisi atau operasi tertentu
angka = [x**2 for x in range(5)]
print(angka)  # Output: [0, 1, 4, 9, 16]