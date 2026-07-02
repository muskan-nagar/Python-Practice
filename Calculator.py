#CALCULATOR PROGRAM:
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def Calculator():
    while True:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

        choice= int(input("Enter your choice:"))
        if choice==5:
            print("THANK YOU !GOODBYE.")
            break
        if choice in (1,2,3,4):
            try:
                n1=int(input("enter first no.:"))
                n2=int(input("enter second no.:"))
            except ValueError:
                print("Invalid input .Please try again.")
                continue
            if choice==1:
                print(f"{n1}+{n2} is '{n1+n2}'")
            elif choice==2:
                print(f"{n1}-{n2} is '{n1-n2}'")
            elif choice==3:
                print(f"{n1}*{n2} is '{n1*n2}'")
            elif choice==4:
                print(f"{n1}/{n2} is '{n1/n2}'")    
        else:
            print("Invalid choice. Choose a valid option")
Calculator()