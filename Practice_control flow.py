print("Date- December 2, 2025")
print("\nPractice of CONTROL FLOW")
print("\n1.SEQUENTIAL STATEMENT")# Logical statements in specific order, where break in logic wil create error.
print("\nEXAMPLE-1")

a=20
b=10
c=a-b
print("Subtraction is:",c)

print("\n2.SELECTION and DECISION")
print("\nSome Decision control Statements are: Simple if, if-else, nested if, if-elif-else")

print("\n2.1 SIMPLE IF statement:")
n=10
if n % 2 == 0:
    print(f"{n} is an even number")

print("\n2.2 IF - ELSE Statement")

print("\nExample 1")

n=1

if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")

print("\nExample 2")
n = int(input("\nEnter a number: "))

if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
    
print("\nExample 3")
alpha = input("Enter an Alphabet: ")

if alpha=="a" or alpha=="e" or alpha=="i" or alpha=="o" or alpha=="u":
    print(f"{alpha} is an Vowel")
else:
    print(f"{alpha} is a Consonant")

print("\nExample 4")
age = int(input("\nEnter your age: "))

if age>=18 and age<125:
    print("\nYou are Eligible to CAST your VOTE")
else:
    print("You are NOT ELIGIBLE to CAST your VOTE")

print("\nExample 5")

num = int(input("\nEnter a Number:"))

if num>0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")
