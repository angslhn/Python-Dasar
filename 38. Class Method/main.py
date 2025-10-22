# Class

# Membuat Class
class Math:
    def __ini__(self, a: int, b: int):
        self.a = a
        self.b = b
        
    def __str__(self) -> str:
        return f"Angka pertama adalah {self.a} dan angka kedua adalah {self.b}"
    
    def kali(self, a: int, b: int) -> int:
        return a * b
    
    def bagi(self, a: int, b: int) -> float:
        return a / b
    
    def tambah(self, a: int, b: int) -> int:
        return a + b
    
    def kurang(self, a: int, b: int) -> int:
        return a - b
    
def main():
    math: Math = Math()
    
    try:
        hasil = math.tambah(a=5, b=7)
        print(f"Hasilnya adalah {hasil}")
    except ValueError:
        print("Parameter harus keduanya angka!")
    
if __name__ == "__main__":
    main()