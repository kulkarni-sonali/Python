# n = 1

# while n<=10:
#     print(n,"Sonali")
#     n += 1


n = 1
count1 = 0
count2 = 0



while n<=100:
    if n % 2 == 0:
        print(f"Even:{n}", end = "   ")
        count1+=1
    else:
        print(f"odd:{n}")
    n+= 1
    

print(f"\n\nTotal Even number are: {count1}")
