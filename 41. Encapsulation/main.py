# Encapsulation

class Orang:
    def __init__(self, nama: str, umur: int) -> None:
        self.nama = nama
        self.umur = umur
        
class Pelajar(Orang):
    def __init__(self, nama: str, umur: int, kelas: str) -> None:
        super().__init__(nama, umur)
        self.kelas = kelas

class Matematika(Pelajar):
    def __init__(self, nama: str, umur: int, kelas: str, nilai: int, is_admin: bool = False) -> None:
        super().__init__(nama, umur, kelas)
        self._nilai = nilai
        self.is_admin = is_admin
        
    def lihat_nilai(self) -> int:
        return self._nilai
    
    def ubah_nilai(self, nilai: int) -> int | None:
        if not self.is_admin:
            return print("Anda tidak diizinkan mengubah nilai!")
        
        if not 0 <= nilai <= 100:
            return print("Rentang nilai untuk siswa tidak valid!")
        
        self._nilai = nilai
    
    def status(self):
        if self._nilai >= 65 and self._nilai <= 100:
            print(f"{self.nama} Lulus di Pelajaran Matematika")
        else:
            print(f"{self.nama} Tidak Lulus di Pelajaran Matematika")
            
def main():
    matematika = Matematika(nama="Dean Supardi", umur=16, kelas="IX-A", nilai=55)
    
    matematika.ubah_nilai(90)

    matematika.status()
    

if __name__ == "__main__":
    main()