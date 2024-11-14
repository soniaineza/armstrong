n = int(input("Enter a number:"))
sum = 0 
original = n 

while n > 0:
    digit = n % 10
    sum += digit ** 3
    n = n // 10

if original == sum:
    print(f"{original}is an Armstrong number!")
else:
    print(f"{original}is not an Armsstrong number.")