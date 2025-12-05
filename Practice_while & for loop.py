# print("December 4, 2025")

# print("\nWhile loop")
# print("Example 1 print numbers from 1-10")

# i = 1
# while i<=10:
#     print(i)
#     i+=1

# print("\nExample 2 print only even numbers from 1-10")

# i = 1
# while i<=10:
#     if i % 2 == 0:
#         print(i)
#     i+=1

# print("\nExample 3 print even- odd numbers from 1-10 and also count them")

# i = 1
# count1 = 0
# count2 = 0

# while i <=10:
#     if i % 2 == 1:
#         print(f"Odd: {i}", end=" ")
#         count1+=1
#     else:
#         print(f"Even: {i}")
#         count2+=1
#     i+=1

# print(f"\nTotal odd numbers are: {count1}")
# print(f"Total Even numbers are: {count2}")

# print("\nExample 4: Check if given 3 digit number is Armstrong number")

# num = int(input("\nEnter a 3 digit number:"))
# sum = 0
# temp = num

# while temp>0:
#     digit = temp % 10
#     sum+=digit**3
#     temp //=10

# if num == sum:
#     print(f"{num} is an armstrong number")
# else:
#     print(f"{num} is not a armstrong number")

# print("\nExample 5 Palindrome string " )
# s = input("Enter a string: ")
# s = s.replace(" "," ").lower()

# start = 0
# end = len(s) -1
# flag = True

# while start < end:
#     if s[start]!= s[end]:
#         flag = False
#     start += 1
#     end -= 1

# if flag:
#     print("The string is pallindrome")
# else:
#     print("The string is not a palindrome")

# print("\n Example 6 : to find the result of base^pow")

# base = int(input("Enter a base: "))
# pow = int(input(" Enter a power: "))

# result = 1; i = 1

# if pow ==0:
#     print(f"{base} raised to the power {pow} is {result} ")
# else:
#     while i <= pow:
#         result *= base
#         i += 1
# print(f"{base} raised to the power{pow} is {result}")

# print("\nDecember 5, 2025")

# print("FOR LOOP")
# print("Example 1 write numbers from 1-10")

# for i in range (1,11):
#     print(i)

# print("\nExample 2 print numbers 10-1")

# for i in range(10,0,-1):
#     print(i)

# print("\nExample 3 - Multiplication table, input from user")

# num=int(input("Display Multiplication Table of :"))

# for i in range (1,11):
#     print(num, 'X', i, "=", num*i)

# print("\nExample 4 - Checking the number as prime " )

# num=int(input("\nEnter a Number"))

# if num<=1:
#     print(f"{num} is not a prime number")
# elif num>1:
#     for i in range(2,num):
#         if num % i == 0:
#             print(f"{num} is not prime number")
#             print(f"{i} is the factor of {num}")
#             break
#     else:
#         print(f"{num} is a prime number")

# print("\nExample 5 program for HCF")

# num1=int(input("Enter the first number"))
# num2=int(input("Enter second number"))

# if num1 < num2:
#     smaller = num1
# else:
#     smaller = num2

# for i in range (1,smaller+1):
#     if ((num1 % i == 0) and (num2 % i == 0)):
#         hcf=i
# print(f"The HCF is {hcf}")

# print("\n Program to print the FIBONACCI sequence")

# terms=int(input("\nEnter the number of terms: "))

# n1,n2 =0,1

# if terms<=0:
#     print("Please enter a positive integer")

# elif terms == 1:
#     print(f"Fibonnaci Sequence : {n1}")
# else:
#     for term in range(terms):
#         print(n1,end=" ")
#         n = n1 + n2
#         n1 = n2
#         n2 = n

# print("\n NESTED FOR LOOP")

# print("Example 1")

# rows = int(input("Enter number of rows: "))

# for i in range (1,rows+1):
#     for j in range(1,rows+1):
#         print("$ ", end = "")
#     print()

# print("\n Example 2")

# rows = int(input("Enter number of rows: "))

# for i in range(1,rows+1):
#     for j in range(1, i+1):
#         print("$", end = "")
#     print()

print("\n Example 5")

rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(" ", end = "")
    for j in range(1, i+1):
        print("$ ", end = "")
    print()

 
# print("\n Example 6")

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows+1):
#     for j in range(1, rows-i+1):
#         print(" ", end = "")
#     for j in range(1, rows+1):
#         print("$", end = "")
#     print()

print("\n Example 7")

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, rows-i+1):
        print(" ", end = "")
    for j in range(1, i+1):
        print("$ ", end = "")
    print()

# print("\n Example 8")

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):
#     for j in range(1, rows-i+1):
#         print(" ", end = "")
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()