# try, except, else, dan finally
# Mencegah program berhenti secara tiba-tiba saat terjadi error dengan menangkap dan mengatasinya

# try       →  Menjalankan kode yang mungkin error
# except    →  Menangkap dan menangani error agar program tetap berjalan
# else      →  Dijalankan jika tidak ada error
# finally   →  Selalu dieksekusi, berguna untuk cleanup seperti menutup file atau koneksi

# Kesalahan tipe data            →  TypeError, ValueError, AttributeError
# Kesalahan indeks atau key      →  IndexError, KeyError
# Kesalahan variabel atau modul  →  NameError, ImportError, ModuleNotFoundError
# Kesalahan file atau iterasi    →  FileNotFoundError, StopIteration
# Kesalahan sintaks & runtime    →  IndentationError, RuntimeError

from math import nan

hasil = nan

try :
    angka_pertama = int(input(' Angka Pertama = '))
    angka_kedua = int(input(' Angka Kedua   = '))
    
    hasil = angka_pertama + angka_kedua
except ValueError:
    print(f'\n Anda harus memasukan angka agar program dapat berjalan.\n')
else:
    print(f'\n Hasil penjumlahan adalah {hasil}\n')   