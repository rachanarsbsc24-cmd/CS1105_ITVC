#Multiples of 3 or 5

sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i

print(sum)

# Even Fibonacci Numbers

a=1
b=2
sum=0

while a<=4000000:
    if a%2==0:
        sum=sum+a
    a,b = b,a+b
print(sum)

