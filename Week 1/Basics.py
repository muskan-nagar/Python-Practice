#BASICS
name=input("enter name:")
age=int(input("enter age:"))
city=input("enter city:")
print(f"HI! I am {name} from {city} . My age is {age}.")
#
n1=int(input("enter num 1:"))
n2=int(input("enter num 2:"))
n3=int(input("enter num 3:"))
avg=(n1+n2+n3)/3
print("Average:",avg)
#
n=int(input("enter no:"))
i=1
while i<=10:
    print(n*i)
    i=i+1
#
n1=10
n2=3
r=n1/n2
q= (n1-r)/n2  # n1= n2*q + r
print(f"Quotient: {q:.2f}, Remainder: {r:.2f}") 

#DISCOUNT CALCULATOR
price= 1200
discount= 15
Disc=int(price *discount/100)
fp=int(price-Disc)
print(f"Discount = {Disc} \nFinal Price = {fp}")

#BMI CALCULATOR
weight= float(input("enter weight in kg:"))
height= float(input("enter height in m:"))
BMI= weight/(height*height)
if BMI< 18.5:
    print("underwight")
elif BMI>=18.5 and BMI<=24.9:
    print("healthy")
elif BMI>=25.0 and BMI<=29.9:
    print("overweight")
elif BMI>30.0:
    print("obese")