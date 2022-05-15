# Q1.
string1 = "Python is a case sensitive language"   #string1
print("<A> THE LENGTH OF STRING IS ", len(string1))  # Function to find LENGTH OF STRRING
print("<B> THE REVERSED STRING IS ", string1[::-1])   # Function to find REVERSED STRING
string2 = string1[10:26]   # STORED a case sensitive IN A NEW STRING
a = string1.replace("a case sensitive" , "object oriented")   # REPLACED "a case sensitive" WITH "object oriented"
print(a)
print("<E> THE INDEX OF SUBSTRING a is ", string1.find('a'))  # Function to find INDEX OF A SUBSTRING
print("<F> THE ORINGINAL STRING AFTER REMOVING WHITESPACES IS", string1.replace(" ",""))
print("\n")


# Q2.
NAME = input("ENTER YOUR NAME")
SID = int(input("ENTER YOUR SID"))
DEPARTMENT = input("ENTER YOUR DEPARTMENT")
CGPA = float(input('ENTER YOUR CGPA'))
print("Hey %s, "% NAME, "Here!")
print("My SID is %d" %SID)
print(" I am from %s" % DEPARTMENT, "and my CGPA is %f" %CGPA)                   
print("\n")                   


# Q3.
a = 56
b = 10
print(a&b)
print(a|b)
print(a^b)
print("Left shift both a and b with 2 bits respectively are :", a<<2, b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are :", a>>2, b>>4)
print("\n")


# Q4.
s = input("ENTER A STRING")
if 'name' in s:
    print("yes")
else:
    print("no")
print("\n")


# Q5.
a = int(input("ENTER FIRST SIDE OF TRIANGLE"))
b = int(input("ENTER SECOND SIDE OF TRIANGLE"))
c = int(input("ENTER THIRD SIDE OF TRIANGLE"))        
if (a >= (b+c)):  # Equality sign is used because if sum of two sides is equal to third side then also triangle is not valid
    print("No")
elif(b >= (a+c)):
    print("No")
elif(c >= (a+b)):
     print("No")
else:
    print("Yes")
print("\n")


# Q6.
# Get the value of a and b
a = int(input("Enter the Value of a: "))
b = int(input("Enter the Value of b: "))
# Calculating xor of a and b
num = a^b
Count_flipped_bit = 0
# Counting Number of set bit present
while (num != 0):
   num = num & (num -1)
   Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)
