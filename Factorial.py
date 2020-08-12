n = int(input("Enter a number : "))

if n<0:
    print("Enter a positive number")
    exit()

def fact(n):

    if n == 0:
        return 1
    return n*fact(n-1)

print("Factorial of",n,"is",fact(n))