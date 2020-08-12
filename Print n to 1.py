n = int(input("Enter a number : "))
if n<=0:
    print("Enter a positive number")
    exit()

def fun(n):
    print(n)

    if n==1:
        exit()
    fun(n-1)

fun(n)
