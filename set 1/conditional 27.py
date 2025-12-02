# a = 5
# b = 10
# c = 15

# if a>b:
#     if a>c:
#         print("a value is big")
#     else:
#         print("c value is big")
# elif b>c:
#     print("b value is big")
# else:
#     print("c value is big")

# a = int(input("Enter a Number: "))
# b = int(input("Enter another Number: "))
# c = int(input("enter another number: "))

# if a>b:
#     if a>c:
#         print("a value is big")
#     else:
#         print("c value is big")
# elif b>c:
#     print("b value is big")
# else:
#     print("c value is big")

# num1 = int(input("enter the 1st number: "))
# num2 = int(input("enter the 2nd number: "))
# num3 = int(input("enter the 3rd number: "))

# if num1>num2 and num2>num3:
#     print(f"{num1} is the greatest number")
# if num2>num1 and num2>num3:
#     print(f"{num2} is the greatest number")
# if num3>num1 and num3>num2:
#     print(f"{num3} is the greatest number")
# if num1<num2 and num1<num3:
#     print(f"{num1} is the smallest number")
# if num2<num1 and num2<num3:
#     print(f"{num2} is the smallest number")
# if num3<num1 and num3<num2:
#     print(f"{num3} is the smallest number")
    
# num = int(input("enter a number: "))

# if num>0:
#     print(f"{num} is positive number")
# elif num == 0:
#     print(f"{num} is neutral number")
# else:
#     print(f"{num} is negative numebr")

# per = eval(input("enter your percentage:"))

# if per<=100 and per>=90:
#     print(f"with a score of {per}%, you have earned  A+ grade")
# elif per<90 and per>80:
#     print(f"with a score of {per}%, you have earned  A grade")
# elif per<80 and per>70:
#     print(f"with a score of {per}%, you have earned B grade")
# elif per<70 and per>50:
#     print(f"with a score of {per}%, you have earned C grade")
# elif per>50 and per<35:
#     print(f"with a score of {per}%, you have earned D grade")
# else:
#     print("Failed")

print("BLOOD DONATION ELIGIBILITY CHECKER")

Name = input("Enter your Name: ")
Age = int(input("Enter your age: "))

if Age>18 and Age<=50:
    print("GREAT!")
    Weight = int(input("Enter your Weight in kg: "))
    if Weight>=50 and Weight<=90:
        print("GREAT! You are ELIGIBLE for Blood Donation")
        print("THANK YOU!")
    else:
        print("NOT ELIGIBLE FOR BLOOD DONATION, You do not follow weight criteria")
        print("THANK YOU!")
else:
    print("NOT ELIGIBLE FOR BLOOD DONATION, You do not qualify age criteria. ")


