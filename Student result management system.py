#Student result management system
name=input("enter name:")
rollno=int(input("enter roll no:"))
eng=int(input("enter marks in english:"))
maths=int(input("enter marks in maths:"))
science=int(input("enter marks in science:"))
hindi=int(input("enter marks in hindi:"))
social=int(input("enter marks in social:"))
Total= eng+maths+science+hindi+social
Percentage=(Total*100)/500
if Percentage>=90:
    Grade="A"
elif Percentage>=80 and Percentage<90 :
    Grade="B"
elif Percentage>=70 and Percentage<80:
    Grade="C"
elif Percentage>=60 and Percentage<=70:
    Grade="D"
elif Percentage>=50 and Percentage<=60:
    Grade="E"
else:
    Grade="Null"

if Grade=="Null":
    Status="Fail"
elif Grade!="Null":
    Status="Pass"

print(f"Name: {name} \nRoll No: {rollno} \nTotal: {Total}\nPercentage: {Percentage}% \n\nGrade: {Grade}\nStatus: {Status}")