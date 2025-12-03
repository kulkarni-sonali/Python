# print("Date- December 2, 2025")
# print("\nPractice of CONTROL FLOW")
# print("\n1.SEQUENTIAL STATEMENT")# Logical statements in specific order, where break in logic wil create error.
# print("\nEXAMPLE-1")

# a=20
# b=10
# c=a-b
# print("Subtraction is:",c)

# print("\n2.SELECTION and DECISION")
# print("\nSome Decision control Statements are: Simple if, if-else, nested if, if-elif-else")

# print("\n2.1 SIMPLE IF statement:")
# n=10
# if n % 2 == 0:
#     print(f"{n} is an even number")

# print("\n2.2 IF - ELSE Statement")

# print("\nExample 1")

# n=1

# if n % 2 == 0:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")

# print("\nExample 2")
# n = int(input("\nEnter a number: "))

# if n % 2 == 0:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")
    
# print("\nExample 3")
# alpha = input("Enter an Alphabet: ")

# if alpha=="a" or alpha=="e" or alpha=="i" or alpha=="o" or alpha=="u":
#     print(f"{alpha} is an Vowel")
# else:
#     print(f"{alpha} is a Consonant")

# print("\nExample 4")
# age = int(input("\nEnter your age: "))

# if age>=18 and age<125:
#     print("\nYou are Eligible to CAST your VOTE")
# else:
#     print("You are NOT ELIGIBLE to CAST your VOTE")

# print("\nExample 5")

# num = int(input("\nEnter a Number:"))

# if num>0:
#     print(f"{num} is a positive number")
# else:
#     print(f"{num} is a negative number")


# print("\nDate - December 3, 2025")
# print("\n 2.3 NESTED IF PROGRAM")
# print("\nNested if programs - when we have to check two or more conditions are true, where one if is under another if ")
# print("\nEXAMPLE 1 ")
# print(".....................")

# a=5
# b=8
# c=3
# if a>b:
#     if a>c:
#         print("a value is big")
#     else:
#         print("c value is big")
# elif b>c:
#     print("b value is big")
# else:
#     print("c value is big")

# print("\nEXAMPLE 1.1 ")
# print(".....................")

# a = int(input("\nEnter a number ")) # inspite of not giving : after statement under bracket, code still runs, how?
# b = int(input("Enter another number "))
# c = int(input("Enter the 3rd number "))

# print("\n                 ")
# if a>b:
#     if a>c:
#         print(" a value is big ")
#     else:
#         print("c value is big ")
# elif b>c:
#     print("b value is big ")
# else:
#     print("c value is big ")

print("\nExample -2 ") # can use in comparative studies 

num1 = int(input("\nEnter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1>num2 and num2>num3:
    print(f"{num1} is the greatest number ")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest number ")
elif num3>num1 and num3>num2:
    print(f"{num3} is the greatest number")
elif num1<num2 and num1<num3:
    print(f"{num1} is the smallest number")
elif num2<num1 and num2<num3:
    print(f"{num2} is the smallest number")
if num3<num1 and num3<num2:
    print(f"{num3} is the greatest number")




"""
print("\n 2.4 IF - ELIF - ELSE PROGRAM")
print("\nThe if-elif-else statement is used to conditionally execute a statement or a block of statemnets.")
print("\nExample 1")
num = int(input("\nEnter a number: "))

if num>0:
    print(f"{num} is positive number")
elif num==0:
    print(f"{num} is positive number")
else:
    print(f"{num} is negative number")

print("\nExample 2 Evaluate the percentage")

per = eval(input("\nEnter your percentage: "))

if per<=100 and per>=90:
    print(f"With a score of {per}%, you have earned  A+ Grade :))")
elif per<90 and per>=80:
    print(f"With a score of {per}%, you have earned  A grade :) ")
elif per<80 and per>=70:
    print(f"With a score of {per}%, you have earned  B Grade ;) ")
elif per<70 and per>=50:
    print(f"With a score of {per}%, you have earned  C Grade ;( ")
elif per<50 and per>=35:
    print(f"with a score of {per}%, you have earned  D Grade :( ")
else:
    print("FAILED! WORK HARD NEXT TIME!")

print("\nExample 3 Program for OPTION SELECTION")

num1 = eval(input("\nEnter a number: "))
num2 = eval(input("Enter another number: "))

print("----Choose one of the option----")
print("\n1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")

Option = int(input("\nEnter your OPTION: "))

if Option == 1:
    print(f"\nAddition of {num1} and {num2} is {num1+num2}")
elif Option == 2:
    print(f"\nSubtraction of {num1} and {num2} is {num1-num2}")
elif Option == 3:
    print(f"\nMultiplication of {num1} and {num2} is {num1*num2}")
elif Option == 4:
    print(f"\nDivision of {num1} and {num2} is {num1/num2}")
else:
    print("Invalid option Selection")
    print("Select the correct option in the range of 1-4")
    


"""



age = 18

print(id(age))