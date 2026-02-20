import SonaliFunctions as SF

#print(SF.Add(1,2))
#print(SF.Sub(4,3))

# BUILT-IN MODULE( MATH MODULE)

import math


#1.floor()  Smallest integral smallest than number
print(math.floor(2.3)) #2

#2. ceil()  smallest integral greater than number
print(math.ceil(2.3)) #3

# 3. cos()  cosine of v alue passed as argument
print(math.cos(math.radians(180)))  #-1
print(math.cos(math.radians(0)))    #1

#4. fabs()  absolute or positive value
print(math.fabs(10))    #10
print(math.fabs(-20))   #20

# 5. factorial()    absolute or positive value
print(math.factorial(5))

# 6. sqrt() the square root of x for x>0
print(math.sqrt(100))   #10
print(math.sqrt(25))    #5
print(math.sqrt(5))     #2.23606797749979


# BUILT-IN MODULE (RANDOM MODULE)
#   Generate or manipulate random numbers through random modules
# 
# 1. choice()   Random items from a list ,tuple, string

import random
l1=[10,20,30,40,50]
print(random.choice(l1))    # any random number from given list 

string="python"
print(random.choice(string))    # any letter from the word "python"

# 2. randrange()    any random number from given range
# randomrange(start,end,step)

# use randrange()function to generate in range from 20 to 50

print(random.randrange(1,100,2))    # any n umber between 1-100


# 3. shuffle()  shuffle a sequence list[]. changing the positio of element
# random.shiffle(sequence)

list1=[10,20,30,40,50]
print("Shuffling number list: ")
random.shuffle(list1)
print(list1)

#list2 = ['A','B','C','D','E']
       # print("Shuffling character list: ")
#random.shuffle(list2)
#print(list2)

# 4. random()   random number between0.0 and 1.0
# random.random()

print(random.random())  #0.5004993670900842

# 5. sample()   any 3 items from list
# random.sample(sequence,k)

mylist = ["Apple", "Banana", "Cherry", "Mangoo", "Pineapple"]
print(random.sample(mylist,k=3))    # ['Pineapple', 'Apple', 'Banana'] any 3 items from list


# 6. uniform()  Random floating numbers between 2 specified numbers ( both included)
# random.unifrom(20,50) any 2 numbers

print(random.uniform(20,50))    #26.159249403393105 any random decimal or whole number


# * BUILT IN MODULE ( DETERMINE MODULE)
# * It deals with date, times and time intervals. date and datetime in python are the objects, 
# so when you manipulatethem, you areb actually manipulating objects and not string or timestamps. 
# * Whenever you manipulate dates or time, you need to import datetime function.

# Example 1 - To get current date 

import datetime
ob=datetime.date.today()
print(ob)

# Example 1 - To get current date and time
import datetime

#ob=datetime.datetime.date.now()   # This function has been discontinued
#print(ob)
ob=datetime.datetime.now().date()
print(ob)
ob=datetime.datetime.now()
print(ob)

# DATE CLASS  # Date in the format of YYYY-MM-DD
# SYNTAX - classdatetime.date(year, month ,day)

from datetime import date

Today=date.today()

print("Current date =", Today)
print("Current Year =", Today.year)
print("Current Day = ", Today.day)

# TIME CLASS
from datetime import time

time(hour=0, minute=0, second=0)
a = time()
print("a= ",a)

#time(hour, minute and second)
b=time(15,30,56)
print("b=",b)
print("Hour= ",b.hour)
print("Minute = ",b.minute)
print("second =", b.second)
print("Microsecond= ",b.microsecond)

#time(hour,minute and second)
c=time(hour=15, minute=30, second=56)
print("c=",c)

#time(hour,minute, second, microsecond)
d=time(15,30,56,234566)
print("d=",d)

#DATETIME CLASS

from datetime import datetime
today=datetime.now()
print("current Date and Time is ", today)

#datetime(year,month,day)
a=datetime(2021,2,6)
print(a)

#datetime(year,month,day,hour,minute,second,microsecond)
b=datetime(2021,2,6,15,30,56,342380)
print(b)

# TIMEDATE CLASS
# Difference between two dates and times

D1=date.today()
D2=date(year=2004, month=3,day=30)

D3=D1-D2
print("D3=",D3)

T1=datetime(year=2001,month=2,day=6,hour=7,minute =9, second=33)
T2=datetime(year=2020, month=12,day=10,hour=5,minute=55,second=13)
T3=T1-T2
print("T3= ",T3)
T4=T2-T1
print("T4=",T4)





