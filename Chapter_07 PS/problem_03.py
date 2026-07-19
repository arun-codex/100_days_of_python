# 1. Write a program to print multiplication table of a given number using for loop.
# 3. Attempt problem 1 using while loop.

table = int(input("Enter a number to get multiplication table: "))

i = 1

while i < 11: 
    print(f"{table} x {i} = {table * i}")
    i +=1

