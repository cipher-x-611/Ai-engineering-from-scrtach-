class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Ali", 20)
student2 = Student("Ahmed", 22)
print("Student 1 Name:", student1.name)
print("Student 1 Age:", student1.age)
print("Student 2 Name:", student2.name)
print("Student 2 Age:", student2.age)