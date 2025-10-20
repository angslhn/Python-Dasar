# Inheritance

# Membuat Class
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def info(self) -> None:
        print(f"Name = {self.name}")
        print(f"Age  = {self.age}")
        

# Pewarisan dari Person
class Student(Person):
    def __init__(self, name: str, age: int, student_id: int) -> None:
        super().__init__(name, age) # panggil constructor dari class induk (Person)
        self.student_id = student_id
    
    def info(self) -> None:
        super().info()
        print(f"Student ID = {self.student_id}")
        

def main():
    data: Student = Student(name="Aang Solihin", age=20, student_id=240160121001)
    data.info()
    
if __name__ == "__main__":
    main()