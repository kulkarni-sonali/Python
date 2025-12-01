# for j in range(1,6):
#     print("* ",end="")
# print()
# for j in range(1,6):
#     print("* ",end="")
# print()
# for j in range(1,6):
#     print("* ",end="")
# print()
# for j in range(1,6):
#     print("* ",end="")
# print()
# for j in range(1,6):
#     print("* ",end="")
# print()


rows = int(input("Enter the number of Rows: "))

for i in range(1,rows+1):
    for j in range(1, rows-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()



# rows = int(input("Enter number of rows: "))

# for i in range (rows,0,-1):
#     for j in range (1, i+1):
#         print("* ", end = "")
#     print()



# rows = int(input("Enter number of rows: "))

# for i in range (1,rows+1):
#     for j in range(1, i+1):
#         print(i, end = " ")
#     print()



# rows = int(input("Enter number of Rows: "))

# for i in range (1,rows+1):
#     for j in range (1, rows-i+1):
#         print(" ", end = "")
#     for j in range(1,i+1):
#         print("* ", end = "") # space after * is necessary
#     print()

# rows = int(input("Enter number of rows: "))

# for i in range(1,rows+1):
#     for j in range(1, rows-i+1):
#         print(" ", end = "")
#     for j in range (1, rows+1):
#         print("* ", end = "")
#     print()

