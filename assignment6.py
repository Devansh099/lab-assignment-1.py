# Q1.
# Check whether the number is perfect or not
# A perfect number is equal to sum of its proper Divisors

def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n%i ==0:
            sum = sum + i
    return sum
n = int(input("Enter a number:"))
s = perfect_number(n)
if n==s:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
print("\n")

# Q2.
# Check Whether a string is palindrome or not


def is_palindrome(s):
    if len(s)<1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a = str(input("Enter a string"))
if (is_palindrome(a)==True):
    print("String is a palindrome")
else:
    print("String is not a palindrome")
print("\n")


#Q3.
#Print out first n rows of Pascal's Triangle
def factorial(m):
    s = 1
    for i in range(1,m+1):
        s*=i
    return s
def pascal_Triangle(n):
    for i in range(1,n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)),end = " ")

        print()    
                    
N = int(input("Enter the number"))
pascal_Triangle(N)
print("\n")


# Q4.
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset<= set(str1.lower())
print(ispangram('The quick brown fox jumps over a lazy dog'))
print("\n")

# Q5.
def word(x):
    for i in range(len(x)+1):
        for j in range(len(x)-1):
            if x[j][0]>x[j+1][0]:
                x[j],x[j+1] = x[j+1],x[j]
    string = ("-").join(x)
    print("Sequence after sorting :-",string)
str = input("Enter hyphen-separated sequence of words :-")
a = str.split("-")
word(a)
print("\n")



# Q6.
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name'in kwargs:
        print(f"sStudent Name: $ {kwargs['student_name']}")
    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name: $ {kwargs['student_name']}")
        print(f"Student Class : $ {kwargs['student_class']}")
student_data(student_id = '21102023',student_name = 'Devansh Kingra')
student_data(student_id = '21102023',student_name = 'Devansh kingra',student_class = 'civil branch')



# Q7.
class Student():
    pass
class Marks():
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1 , Student))
print(isinstance(marks1 , Marks))
print(isinstance(student1, Student))
print("\nCheck whether the said classes are the sub classes of the built in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()


# Q8.
class py_solution():
    def threesum(self,nums):
        nums, result, i = sorted(nums), [], 0
        while i<len(nums)-2:
            j, k = i+1, len(nums)-1
            while j<k:
                if (nums[i] + nums[j] + nums[k])<0:
                    j+=1
                elif (nums[i] + nums[j] + nums[k])>0:
                    k-=1
                else:
                    result.append(nums[i])
                    result.append(nums[j])
                    result.append(nums[k])
                    j, k =  j+1, k-1
                    while j<k and nums[j]== nums[j-1]:
                        j+=1
                    while j<k and nums[k]== nums[k+1]:
                        k-=1
            i +=1
            while i<len(nums)-2 and nums[i] == nums[i-1]:
                   i+=1
        return result
print(py_solution().threesum([-25, -10, -7, -3, 2 , 4, 8, 10]))
print()


# Q9.
class paranthesis:
    def find(str):
        a = ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str
s = input("Enter the sequence of paranthesis:")
if paranthesis.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")
    
        
    
    


    



    
        
           

