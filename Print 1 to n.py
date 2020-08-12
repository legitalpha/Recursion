n = int(input("Enter a number : "))
i=1
def fun(i):
    print(i)

    if i==n:
        exit()
    fun(i+1)


fun(i)