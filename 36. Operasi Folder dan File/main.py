# Semua operasi folder dan file

import os
import shutil
import glob
import zipfile
import subprocess
from pathlib import Path
import time

### 1. Membaca dan Menelusuri Folder

# Menampilkan daftar file & subfolder dalam folder tertentu
base_path = os.getcwd()  # Mengambil folder saat ini
print("Daftar isi folder:", os.listdir(base_path))

# Dapatkan path folder main.py
base_path = os.path.dirname(os.path.abspath(__file__))
print("Main.py berada di folder:", os.listdir(base_path))

# Menelusuri semua file dalam folder dan subfolder dengan os.walk()
for root, dirs, files in os.walk(base_path):
    for file in files:
        print(os.path.join(root, file))

# Menggunakan glob untuk mencari file dengan pola tertentu
file_list = glob.glob("**/*.txt", recursive=True)
print("File dengan ekstensi .txt:", file_list)

# Menggunakan pathlib untuk pencarian yang lebih Pythonic
file_list = [str(file) for file in Path(base_path).rglob("*.txt")]
print("File .txt menggunakan pathlib:", file_list)

### 2. Membuat, Menghapus, dan Mengubah Folder

# Membuat folder baru
os.makedirs("folder_baru", exist_ok=True)
print("Folder dibuat: folder_baru")

# Menghapus folder
shutil.rmtree("folder_baru", ignore_errors=True)
print("Folder dihapus: folder_baru")

# Mengubah nama folder
if os.path.exists("folder_lama"):
    os.rename("folder_lama", "folder_baru")
    print("Folder diubah namanya")

### 3. Operasi File dalam Folder

# Menyalin file
shutil.copy("source.txt", "destination.txt")
print("File disalin")

# Memindahkan file
shutil.move("source.txt", "folder_baru/source.txt")
print("File dipindahkan")

# Menghapus file
if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("File dihapus")

### 4. Mengecek Properti File & Folder

# Mengecek apakah file/folder ada
print("Apakah file.txt ada?", os.path.exists("file.txt"))
print("Apakah folder_baru adalah folder?", os.path.isdir("folder_baru"))
print("Apakah file.txt adalah file?", os.path.isfile("file.txt"))

# Mendapatkan ukuran file
if os.path.exists("file.txt"):
    print("Ukuran file.txt:", os.path.getsize("file.txt"), "bytes")

# Mendapatkan waktu modifikasi terakhir
if os.path.exists("file.txt"):
    print("Waktu modifikasi:", time.ctime(os.path.getmtime("file.txt")))

### 5. Operasi Zip & Arsip

# Membuat file zip dari folder
shutil.make_archive("backup", "zip", "folder_asli")
print("Folder telah diarsipkan ke backup.zip")

# Mengekstrak file zip
with zipfile.ZipFile("backup.zip", "r") as zip_ref:
    zip_ref.extractall("folder_tujuan")
print("File ZIP diekstrak")

### 6. Menjalankan Perintah Sistem pada Folder/File

# Menjalankan perintah shell (Linux/Windows)
subprocess.run("ls" if os.name == "posix" else "dir", shell=True)

print("\nOperasi selesai.")
