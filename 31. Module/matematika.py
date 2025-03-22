def tambah (a:int, b:int) -> int:
    return a + b

def kurang (a:int, b:int) -> int:
    return a - b

def kali (a:int, b:int) -> int:
    return a * b

def bagi (a:int, b:int) -> int:
    return a + b

def rata_rata (*nilai:int) -> int:
    hasil_nilai = 0
    for angka in nilai:
        hasil_nilai += angka
    return round(hasil_nilai / len(nilai))