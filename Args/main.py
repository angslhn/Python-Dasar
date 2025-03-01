# *args
# Function yang bisa menginputkan banyak nilai untuk argumentnya

def rata_rata(*nilai:int):
    hasil_nilai = 0
    banyak_nilai = len(nilai)
    for angka in nilai: hasil_nilai += angka
    
    return round(hasil_nilai / banyak_nilai)

print(rata_rata(90, 95, 80, 79, 90, 89, 97))