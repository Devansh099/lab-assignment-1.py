# Q1.
m = float(input("Enter your marks:"))
if (m <25):
    print("F")
elif(m >=25 and m <45):
    print("E")
elif(m >=45 and m <50):
    prrint("D")
elif(m >=50 and m <60):
    print("C")
elif(m >=60 and m <80):
    print("B")
elif(m >=80):
    print("A")
print("\n")    
          

# Q2.
a = int(input("Enter year:"))
if a % 400 == 0 :
        print(a, "is a Leap Year")
elif(a % 100 == 0):
    print(a, "is not a Leap Year")
elif(a % 4 == 0):
    print(a, "is a leap year")
else:
    print(a, "is not a leap year")
print("\n")


# Q3.
import random
for i in range(1,11,1):
    num1 = random.randrange(1,10,1)
    num2 = random.randrange(1,10,1)

    print("The multiplication problem is",num1, "*", num2)
    guess = int(input("What is your guess?"))

    if guess == num1*num2:
        print("Answer is correct!")
    else:
        print("Answer is not correct!, The correct answer is ", num1*num2)
print("\n")

# Q4. Determining the Total number of candies
n = 1
while n < 200:
    if n%5==2 and n%6==3 and n%7==2:
        print("Number of candies in the box are",n)
        break
    else:
        n+=1

        

    



   
    
