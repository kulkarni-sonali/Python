print("Date December 2, 2025")

print("\n1. WRITE A PROGRAM FOR ADDITION - DELETION")

a = 5
b = 7

print("\nAddition is:", a+b) #\n is for new line
print("\nSubtraction is:", a-b)


print("Addition is:", a+b) # without new line order
print("Subtraction is:", a-b)

print("\n2. Write a program for functions of  Addition, Subtraction, Multiplication, Division, Modulus, Floor Division, Exponential")

num1 = int(input("\nEnter a Number: "))
num2 = int(input("Enter an another Number: "))

print(f"\nAddition of {num1} and {num2} is {num1+num2}") # \n order placed to make gap after data and starting this code seperately from data.
print(f"Subtraction of {num1} and {num2} is {num1-num2}")
print(f"Multiplication of {num1} and {num2} is {num1*num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")
print(f"Modulus of {num1} and {num2} is {num1%num2}")
print(f"Floor Division of {num1} and {num2} is {num1//num2}")
print(f"Exponential of {num1} and {num2} is {num1**num2}")


print("\n3. Write a program to find Area of Circle")

radius = int(input("\nEnter the Value of radius: "))

Area = 3.14 * (radius**2) # pai * radius ^2, where value of pai id 22/7 or 3.14
print(f"\nArea of circle is: {Area}")

