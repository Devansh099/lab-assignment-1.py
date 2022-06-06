# Q1.
a = int(input("ENTER YOUR NUMBER :"))
b = bin(a)
print(b)
print("\n")

# Q2.
print('Implementing a simple calculator Emulation')
print('The program exists when an incorrect expression is entered or "Quit"')
while True:
    term_math = input('Enter a mathematical expression:')
    if term_math.lower() == 'quit':
        break
    print('Result :',eval(term_math))
print("\n")

# Q3.
print((3+4)*(5))                           #first part
print("\n")

n = int(input("Enter your number:"))       #second part
ans = (n)*(n-1)/2
print(ans)
print("\n")

import math
r=int(input("Enter the radius:"))           #third part
a = 4*(math.pi)
ans = a*(r*r)
print(ans)
print("\n")

import math                                  #fourth part
a = 90
b = 45
r = int(input("Enter value of r:"))
c = float(r*(math.cos(a))*2)
d = float(r*(math.sin(a))*2)
ans = math.sqrt(c+d)
print(ans)
print("\n")

x1 = int(input("Enter the value of x1:"))    #fifth part
x2 = int(input("Enter the value of x2:"))
a = (x2-x1)
y1 = int(input("Enter the value of y1:"))
y2 = int(input("Enter the value of y2:"))
b = (y2-y1)
ans = (b/a)
print(ans)
print("\n")


# Q4.
print("Output of part a:")
for a in range(5):
    print(a , end=" ")
print("\n")    

print("Output of part b:")
for b in range(3,10):
    print(b , end=" ")
print("\n")    


print("Output of part c:")
for c in range(4,13,3):
    print(c , end=" ")
print("\n")    

print("Output of part d:")
for d in range(15,5,-2):
    print(d , end=" ")
print("\n")    

print("Output of part e:")
for e in range(5,3):
    print(e , end=" ")
print("\n")


# Q5.
H = int(input("Enter no of hydrogen atoms:"))
C = int(input("Enter no of carbon atoms:"))
O = int(input("Enter no of oxygen atoms:"))
ans = (1.00794*H + 12.0107*C + 15.9994*O)       
print(ans)
    





    
                







