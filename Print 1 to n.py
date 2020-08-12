n = int(input("Enter a number : "))
i=1
if n<=0:
    print("Enter a positive number")
    exit()
def fun(i):
    print(i)

    if i==n:
        exit()
    fun(i+1)


fun(i)
