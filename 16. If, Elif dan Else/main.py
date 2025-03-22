# If, Elif dan Else

print("-" * 27)
print(" MENGHITUNG NILAI MAHASISWA")
print("-" * 27)

nama = str(input(" Nama        = "))
nilai_tugas = int(input(" Nilai Tugas = " ))
nilai_uts = int(input(" Nilai UTS   = "))
nilai_uas = int(input(" Nilai UAS   = "))

total_nilai = nilai_tugas + nilai_uts + nilai_uas
nilai_akhir = round(total_nilai / 3)

print("-" * 100)
print(f" Selamat {nama} Nilai Total Kamu Di Mata Kuliah Ini Adalah {total_nilai} dan Nilai Akhirnya Adalah {nilai_akhir}")
print("-" * 100)

if nilai_akhir >= 0 and nilai_akhir < 60:
    print(" Kamu Mendapatkan E Didalam Mata Kuliah Ini.")
elif nilai_akhir > 60 and nilai_akhir < 70:
    print(" Kamu Mendapatkan D Didalam Mata Kuliah Ini.")
elif nilai_akhir > 70 and nilai_akhir < 80:
    print(" Kamu Mendapatkan C Didalam Mata Kuliah Ini.")
elif nilai_akhir > 80 and nilai_akhir < 90:
    print(" Kamu Mendapatkan B Didalam Mata Kuliah Ini.")
elif nilai_akhir > 90 and nilai_akhir < 100:
    print(" Kamu Mendapatkan A Didalam Mata Kuliah Ini.")
else:
    print(" Nilai Hasil Akhir Kamu Tidak Valid!")
    
print("-" * 44)