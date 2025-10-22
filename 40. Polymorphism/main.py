# Polymorphism

class Hewan:
    def suara(self) -> str:
        return "Suara Hewan!"
        
class Anjing(Hewan):
    def suara(self) -> str:
        return "Gukk! Gukk! Gukk!"

class Kucing(Hewan):
    def suara(self) -> str:
        return "Meoww! Meoww! Meoww!"

def main():
    semua_hewan: list[Hewan] = [Hewan(), Anjing(), Kucing()]
    
    for hewan in semua_hewan:
        print(hewan.suara())

if __name__ == "__main__":
    main()