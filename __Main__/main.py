# __main__
# Nama khusus yang digunakan untuk menandai script yang sedang dieksekusi secara langsung

def salam(nama:str):
    print(f"Halo {nama}, selamat datang!")

if __name__ == "__main__":
    nama = str(input("Nama Anda = "))
    salam(nama=nama.title())