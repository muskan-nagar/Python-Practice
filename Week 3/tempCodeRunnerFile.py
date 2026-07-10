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