#Q1. program to find average of three numbers entered by the user
a = int(input('Enter first number :'))
b = int(input('Enter second number :'))
c = int(input('Enter third number :'))
avg = (a+b+c)/3
print("average of three numbers is :" ,avg)


#Q2. program to compute a person's income tax
income = float(input("Enter your gross income (to the nearest penny): "))
no_of_dependents = int(input("Enter the number of dependents: "))
taxable_income = income - 1000 - (3000*no_of_dependents)
tax = (taxable_income * 20)/100
print("Your tax is :", tax)                     


#Q3. program to store different data type values into a list
SID = int(input('Enter your SID : '))
Name = str(input('Emter your Name : '))
Gender = str(input('Enter your Gender(M/F/O): '))
Course_name = str(input('Enter your Course: '))
CGPA = float(input('Enter your CGPA: '))
Student = [SID,Name,Gender,Course_name,CGPA]
print(Student)


#Q4. program to enter marks of 5 students into a list and display them in a sorted manner
S1 = int(input('Enter the marks of First student: '))
S2 = int(input('Enter the marks of Second student: '))
S3 = int(input('Enter the marks of Third student: '))
S4 = int(input('Enter the marks of Fourth student: '))
S5 = int(input('Enter the marks of Fifth student: '))
list = (S1,S2,S3,S4,S5)
print(sorted(list))


#Q5. (a) and(b)
color = ['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)
color[3] = 'Purple'
print(color)
