#SQUARE OF A NUMBER
def square(num):
    #num=int(input("enter num:"))
    return num**2   # or num*num
print(square(10))

#CHECKING PRIME NUMBER
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

#CHECKING PRIME NUMBER
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

#AREA OF CIRCLE
def area(r):
    return 3.14*r*r
print(area(5))