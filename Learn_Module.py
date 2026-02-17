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

#list2 = ['A','B,'C','D','E']
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