# Q1. Write a Python program to display first 100 odd numbers and find their sum

sum_odd = 0

for a in range(1,200,2):
    print(a, end=", ")
    sum_odd += a

print("\nSum of first 100 odd numbers=",sum_odd) #Output: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 
Sum of first 100 odd numbers= 10000

# Q2. Write a python program to display the sum of all odd numbers from 1 to 100

sum_odd2 = 0

for i in range(1,101):
    if i%2 !=0:
        sum_odd2 +=i

print(sum_odd2) # Output: 2500


""" Problem Zero: A number is a perfect square, or a square number, if it is the square of a positive integer.
For example,  is a square number because 5^2= 5*5=25 ; it is also an odd square.
The first 5 square numbers are: 1,4,8,16,25, and the sum of the odd squares is 1+9+25=35.

Among the first 820 thousand square numbers, what is the sum of all the odd squares?"""

def sum_of_odd_squares(N):
    total = 0
    for i in range(1, N + 1):
        sq = i * i
        if sq % 2 == 1:
            total += sq
    return total


if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(sum_of_odd_squares(N)) # Output: Enter N: 820000
91894666666530000

