'''
name=input("enter name:")
age=int(input("enter age:"))
city=input("enter city:")
print(f"HI! I am {name} from {city} . My age is {age}.")

n1=int(input("enter num 1:"))
n2=int(input("enter num 2:"))
n3=int(input("enter num 3:"))
avg=(n1+n2+n3)/3
print("Average:",avg)

n=int(input("enter no:"))
i=1
while i<=10:
    print(n*i)
    i=i+1

n1=10
n2=3
r=n1/n2
q= (n1-r)/n2  # n1= n2*q + r
print(f"Quotient: {q:.2f}, Remainder: {r:.2f}") 

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

num=1
for num in range(1,101):
    print(num)

num=1
for num in range(1,101):
    if num%2==0:
        print(num)

sum=1 
for i in range(10):
    sum=sum+i
    print(sum)

i=10
while i>0:
    print(i)
    i=i-1

num =1112
sum =0
while num>0:
    sum=sum

i=1
while i<6:
    print("*"*i)
    i=i+1
i=5
while i>0:
    print("*"*i)
    i=i-1

i=1
while i<10:
    print("*"*i)
    i=i+2

i=0
while i<=5:
'''
'''
def square(num):
    #num=int(input("enter num:"))
    return num**2   # or num*num
print(square(10))

def prime(num):
    #num=int(input("enter num:"))
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is not prime")
                break
        else:
            print(num,"is prime")
    else:
        print(num,"is not prime")
prime(9)

def  prime(num):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is not a prime")
                break
            else:
                print(num,"is a prime")
                break
    else:
        print(num, "not a prime")
prime(-19)

def area(r):
    return 3.14*r*r
print(area(5))
'''
"""

