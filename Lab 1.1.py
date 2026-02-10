# Q1. Write a Python program to display first 100 odd numbers and find their sum

sum_odd = 0

for a in range(1,200,2):
    print(a, end=", ")
    sum_odd += a

print("\nSum of first 100 odd numbers=",sum_odd)

# Q2. Write a python program to display the sum of all odd numbers from 1 to 100

sum_odd2 = 0

for i in range(1,101):
    if i%2 !=0:
        sum_odd2 +=i
print(sum_odd2)