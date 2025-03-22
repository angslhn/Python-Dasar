# Function type hints
# Cara membatasi sebuah fungsi agar hanya bisa memasukan nilai
# tipe data tertentu dan output tipe data tertentu

# Function dengan nilai return
def kali(angka_pertama:int, angka_kedua:int) -> int:
    return angka_pertama * angka_kedua

angka_pertama = 10
angka_kedua = 32

print(f"Perkalian antara {angka_pertama} dan {angka_kedua} hasilnya adalah {kali(angka_pertama, angka_kedua)}")

# Function tanpa nilai return
def show_text(text:str):
    print(f"{text}")
    
show_text("Nama saya adalah Aang Solihin")