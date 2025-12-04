print("December 4, 2025")

print("\nWhile loop")
print("Example 1 print numbers from 1-10")

i = 1
while i<=10:
    print(i)
    i+=1

print("\nExample 2 print only even numbers from 1-10")

i = 1
while i<=10:
    if i % 2 == 0:
        print(i)
    i+=1

print("\nExample 3 print even- odd numbers from 1-10 and also count them")

i = 1
count1 = 0
count2 = 0

while i <=10:
    if i % 2 == 1:
        print(f"Odd: {i}", end=" ")
        count1+=1
    else:
        print(f"Even: {i}")
        count2+=1
    i+=1

print(f"\nTotal odd numbers are: {count1}")
print(f"Total Even numbers are: {count2}")

print("\nExample 4: Check if given 3 digit number is Armstrong number")

num = int(input("\nEnter a 3 digit number:"))
sum = 0
temp = num

while temp>0:
    digit = temp % 10
    sum+=digit**3
    temp //=10

if num == sum:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not a armstrong number")

print("\nExample 5 Palindrome string " )
s = input("Enter a string: ")
s = s.replace(" "," ").lower()

start = 0
end = len(s) -1
flag = True

while start < end:
    if s[start]!= s[end]:
        flag = False
    start += 1
    end -= 1

if flag:
    print("The string is pallindrome")
else:
    print("The string is not a palindrome")

print("\n Example 6 : to find the result of base^pow")

base = int(input("Enter a base: "))
pow = int(input(" Enter a power: "))

result = 1; i = 1

if pow ==0:
    print(f"{base} raised to the power {pow} is {result} ")
else:
    while i <= pow:
        result *= base
        i += 1
print(f"{base} raised to the power{pow} is {result}")