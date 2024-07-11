number = input("Enter a number: ")
number = int(number)
def fact(x):
    out = 1
    for i in range(1, x+1):
        out = out * i
    print(out)
fact(number)
