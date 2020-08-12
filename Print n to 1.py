n = int(input("Enter a number : "))

def fun(n):
    print(n)

    if n==1:
        exit()
    fun(n-1)

fun(n)
