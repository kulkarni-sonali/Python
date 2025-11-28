
print("Numbers from 10 to 1")
for a in range(10,0,-1):
    print(a)


print("Multiplication table, take input from User")
num = int(input("Display Multiplication table of:"))

for m in range(1,13):
    print(num, 'X', m, "=", num*m)


print("Write a program to check whether a given number is prime. ")

print("Prime Number is a Natural Number greater than 1 that has no positive divisors other than 1 and itself.")

print("Example:2,3,5,7,11,13,...... are all prime numbers.")

num = int(input("Enter an Integer: "))

if num <= 1:
    print(f"{num} is not Prime Number.")
elif num > 1:
    for p in range(2,num):
        if num % p == 0:
            print(f"{num} is not a Prime Number.")
            print(f"{p} is the factor of {num}")
            break
    else:
        print(f"{num} is a Prime Number")


print("WRITE A PROGRAM TO FIND THE HCF( HIGHEST COMMON FACTOR) OF TWO NUMBERS")

print("HIGHEST COMMON FACTOR (HCF): The Highest Common factor (HCF) of given numbers is the largest Positive Interger that perfectly divides the given numbers. ")

print("Example: HCF of 12 and 18 is 6 ")
print("Factors of 12: 1,2,3,4,6,12")
print("Factors of 18: 1,2,3,6,9,18 ")

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for h in range(1,smaller + 1):
    if ((num % h == 0) and (num2 % h == 0)):
        hcf=h # store the highest common factor

print(f"The HCF is {hcf}.")


print("WRITE A PROGRAM TO PRINT THE FIBONACCI SEQUENCE")
print("FIBONACCI SEQUENCE is a sequence in which each term can be obtained by adding the previous two terms.")

terms = int(input("Enter the number of terms: "))

n1, n2 = 0, 1

if terms<=0:
    print("Please enter a positive integer")
elif terms == 1:
    print(f"Fibonnaci sequence: {n1}")
else:
    for term in range(terms):
        print(n1,end=" ")
        n = n1 + n2
        n1 = n2
        n2 = n
