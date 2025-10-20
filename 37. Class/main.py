# Class

# Membuat Class
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def info(self) -> None:
        print(f"Name = {self.name}")
        print(f"Age  = {self.age}")
        

def main():
    person: Person = Person(name="Aang Solihin", age=20)
    person.info()
    
if __name__ == "__main__":
    main()