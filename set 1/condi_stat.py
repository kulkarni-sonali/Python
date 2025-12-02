num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a Positive number")
elif num==0:
    print(f"{num} is neither Positive nor Negative")
else:
    print(f"{num} is a Negative number")

# if num % 2 == 0:
#     print(f"{num} is a even number")
# else:
#     print(f"{num} is an Odd number")


# alpha = input("Enter an alphabet:")
# if alpha =="a" or alpha == "e" or alpha == "i" or alpha == "o" or alpha == "u":
#     print(f"{alpha} is a Vowel")
# else:
#     print(f"{alpha} is a consonant")

# age = int(input("enter your age:"))
# if age>=18 and age<125:
#     print("you are eligible to cast your vote")
# else:
#     print("You are NOT eligible to cast your vote")


a = 5
b = 10
c = 15

if a>b:
    if a>c:
        print("a value is big")
    else:
        print("c value is big")
elif b>c:
    print("b value is big")
else:
    print("c value is big")


