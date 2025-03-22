# Tipe data integer
x = 1
print ("Variable dari x = ", x, " tipe datanya adalah ", type(x))

# Tipe data float
y = 1.5
print ("Variable dari y = ", y, " tipe datanya adalah ", type(y))

# Tipe data string
nama_lengkap = "Aang Solihin"
print ("Variable dari nama_lengkap = ", nama_lengkap, " tipe datanya adalah ", type(nama_lengkap))

# Tipe data boolean
result = True
print ("Variable dari result = ", result, " tipe datanya adalah ", type(result))

# Tipe data bilangan complex
nilai = complex(5, 10)
print ("Variable dari nilai = ", nilai, " tipe datanya adalah ", type(nilai))

# Tipe data yang diambil dari module tipe data bahasa C
from ctypes import c_double

angka = c_double(0.435205300000001)
print ("Variable dari angka = ", angka, " tipe datanya adalah ", type(angka))