"""
Week 3 - Object Oriented Programming Practice
Topics:
- Classes and Objects
- Constructors
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction
"""
#Classes and Objects
class empty:
    pass

class Myclass:    #Myclass is class name
    x=10
    y=9
    z=192
p=Myclass()   #p is object
print(p.x)
del p
p1=Myclass()
p2=Myclass()
p3=Myclass()
print(p1.x)
print(p2.z)
print(p3.y)

#__init__() method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("Muskan",18)
print(p.name)
print(p.age)

class Person:
    def __init__(self, name, age=19):
        self.name=name
        self.age=age
p1=Person("Muskan")
p2=Person("Nimish",20)
print(f"{p1.name},{p2.name}")
print(f"{p1.age},{p2.age}")

class Mobile:
    def __init__(self,user_name,company):
        self.user_name=user_name
        self.company=company
m1=Mobile("Sanjay","Redmi")
m2=Mobile("Khushi","Samsung")
print(f"{m1.user_name} has a {m1.company} phone.")
print(f"{m2.user_name} has {m2.company} phone.")

class Students:
    def __init__(self,Name,Roll_no,Branch,CGPA):
        self.name=Name
        self.Rollno=Roll_no
        self.Branch=Branch
        self.cgpa=CGPA
s1=Students("Muskan",101,"AIML",9.5)
s2=Students("Khushi",102,"AI",9.8)
s3=Students("Manshi",103,"CSE",9.7)
print(f"Name:{s1.name}\nBranch:{s1.Branch}\nRoll No.:{s1.Rollno}\nCGPA:{s1.cgpa}")
print("-------------------------------------------")
print(f"Name:{s2.name}\nBranch:{s2.Branch}\nRoll No.:{s2.Rollno}\nCGPA:{s2.cgpa}")
print("-------------------------------------------")
print(f"Name:{s3.name}\nBranch:{s3.Branch}\nRoll No.:{s3.Rollno}\nCGPA:{s3.cgpa}")
print("-------------------------------------------")