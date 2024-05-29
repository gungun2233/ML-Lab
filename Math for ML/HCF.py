a = int(input("Enter a number!"))
b = int(input("Enter another number!"))

dividend = max(a,b)
divisor = min(a,b)

remainder = dividend % divisor 
while remainder!=0:
    dividend = divisor
    divisor = remainder
    remainder = dividend % divisor 

print(divisor)
