#Program to find factorial of a given number.
num = int(input("Enter a number: "))

fact = 1
while num != 0:
    fact = fact*num
    num -= 1

print(fact)