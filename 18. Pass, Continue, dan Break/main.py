# Pass, Continue, dan Break

# Pass
# `pass` digunakan sebagai placeholder. Dalam contoh ini, `pass` sebenarnya tidak memberikan efek apa-apa
# pada logika looping. Biasanya, `pass` digunakan saat Anda belum menentukan kode apa yang akan ditulis.
index = 1
while index <= 10:
    print(f"Ini Looping Ke {index}")
    index += 1
    pass  # Placeholder, tidak memengaruhi logika

# Continue
# `continue` digunakan untuk melompati iterasi berikutnya dalam loop. Dalam contoh ini,
no_index = 1
while no_index <= 10:
    print(f"Ini Looping Ke {no_index}")
    
    no_index += 1
    
    if no_index == 5:
        continue  # Melompati iterasi ini, "Maman Supratman" tidak akan dicetak jika `no_index == 5`
    
    print("Maman Supratman")

# Break
# `break` digunakan untuk menghentikan loop sepenuhnya, meskipun kondisi loop masih True.
angka = 1
while angka <= 10:
    print(f"Angka {angka}")
    
    angka += 1
    
    if angka == 8:
        break  # Menghentikan loop ketika `angka == 8`