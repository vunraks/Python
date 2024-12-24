#task1
class Book:
    def __init__(self, title, author, pages):
       self.title = title
       self.author = author
       self.pages = pages

    def display_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Кол-во страниц: {self.pages}") 

book = Book("Зелёная миля", "Стивен Кинг", 384)   
book.display_info()  




# #task2
class Animal:
    def speak(self):
        print("Animal makes a sound")
animal = Animal()
animal.speak()

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed

    def speak(self):
        print(f"{self.breed} dog barks") 

dog = Dog("Pitbull")
dog.speak()        


#task3
class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def is_excellent(self):
        return self.average_grade >=4.5
    
student = Student("Евгений Каледин", "11`В`", 3)    
print(f"Студент: {student.name} из группы: {student.group} отличник: {student.is_excellent()}")
