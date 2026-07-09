"""
Week 2 - Data Structures Practice
Topics:
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- List Comprehensions
"""
#STRINGS
s="aBCDEF"  #modifying a string
s="A" + s[1:]
print(s)
del s   #deleting a string
print(s)
'''methods of a string'''
a="Hello"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("e","a"))
print(a.strip()) #for removing whitespace from the beginning and end of a string
print(a[0:8:2])#slicing 
print(a.find("l"))
print(a.count("p"))

x=" hi "
y="bye"
z= " "
print(x+z+y) #concatenation
print(x*6) #repetition
print(f"{x} and {y}")
print("y" in y) #membership operator
print("say" in x)
print(x.join(y))

print(y[::-1]) #reversing a string

c="Hello. This is Muskan."
print(len(c.split())) 
print(c.replace(" ", ""))

def is_palindrome(text):
    return text==text[::-1]
print(is_palindrome("hiih"))
print(is_palindrome("my bad"))

#LISTS
'''creating a list'''
a=(1,2,3,4,5)
a=list(a)
print(a)
b=list("abcdefgh")
print(b)
c=['i']*4
print(c)
print(a[3])
d=[1,2,9784.4,"hello"]
print(d[3][4])
 
'''modifying a list'''
a=[1,2,3,4]
a.append("hi")
print(a)
a.insert(2,"hello")
print(a)
a.extend([23,True])
print(a)
a[-1]=False
print(a)
a.remove(1) #removes the value
print(a)
a.reverse()
print(a)
a.pop() #removes the last value or if given value then removes that index
print(a)
del a[0:7:2] #deletes the values from index 0 to 7 with a step of 2
print(a)
a.clear() #removes all the values from the list
print(a)

list=[[1,[33,4,4.56],2] , ["hi", "hello"],[True, False]]
print(list[0][1][2])
for i in list:
    print(i)

values=[23,82,12,90,54]
for i in values:
    avg=sum(values)/len(values)
    break
print(avg)

no=[3,465,14,928,99]
max=no[0]
for i in no:     #finding the largest number
    if i>max:
        max=i
print(max)  
max2=no[0]    #finding the second largest number
for i in no:
    if i<max and i>max2:
        max2=i
print(max2)
print(max(no))  #2
no.sort()      #3
print(no[-1])  