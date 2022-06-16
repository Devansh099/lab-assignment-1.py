# Q1. To reverse the given string
s = input("Enter a string:")    #Taking input from the user
l = len(s)
s2 = ''
for i in range(l-1,-1,-1):
    s2 = s2 + s[i]              #Concatinating character from backwardof the input string to new string
print("Reverse string is:",s2)    
print("\n")

# Q2. To print numbers in a given range divisible by a number
x1,x2 = input("Enter the range of numbers :").split()
x1 = int(x1)
x2 = int(x2)
n = int(input("Enter number:"))
for i in range(x1,x2,1):
    if i%n == 0:    #if it is divisible then print the number
        print(i)
        continue
print("\n")    

# Q3. To find the area of triangle
import math
a = int(input("Enter first side of triangle:"))
b = int(input("Enter second side of trinagle:"))
c = int(input("Enter third side of triangle:"))
if a<0 or b<0 or c<0:
    print("Invalid input, side cannot be negative")
elif(a+b<c or b+c<a or c+a<b):
    print("Combination of sides is not possible")
else:
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Area of the triangle is {area}")
print("\n")


# Q4. To print the star pattern
rows = 5
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end='')
    print()


# For second pattern
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("* ",end='')
    print()


# Q5. To print payttern
rows = int(input("Enter the no of rows:"))
m = 65  #ASCII code of A is 65
for i in range(rows):
    for j in range(i+1):
        if m>90:
            m=65
        print(chr(m),end='')
        m+=1
    print()
print()


# Q6. To print prime numbers in a given range
x1,x2 = input("Enter the range of numbers:").split()
x1 = int(x1)
x2 = int(x2)
for i in range(x1,x2,1):
    c = 0
    n = 1
    while n<=i:
        if i%n == 0:
            c+=1
            n+=1
            continue
        n+=1
    if c==2:
            print(i)
print("\n")


# Q7. To print numbers that are multiple of 7 and divisible by 11 in the range 1-500
for i in range(1,500):
    if i%7==0 and i%11==0:
        print(i)
print("\n")


# Q8.
list =[]
for i in range(0,10,1):
    n = int(input(f"Enter {i+1} number:"))
    list.append(n)
print(list)

#a)
print("Positive numbers are:")
for i in range(10):
    if list[i]>0:
        print(list[i])


#b)
print("NEgative numbers are:")
for i in range(10):
    if list[i]>0:
        print(list[i])


#c)
print("ODd numbers are:")
for i in range(10):
    if list[i]!=0:
        print(list[i])


#d)
print("Even numbers are:")
for i in range(10):
    if list[i]==0:
        print(list[i])



#e)
count = dict()
for no in list:
    if no in count:
        count[no]+=1
    else:
        count[no]=1

print("No of times each number occurs in the list:")
print(count)
print("\n")



# Q9. Count the no of occurnce of each word in the list input by the user

str = input("Enter a string:")
counts = dict()
words = str.split(' ')
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word] = 1
print(counts)        
        
        

        
    

          
    


    
        

        


