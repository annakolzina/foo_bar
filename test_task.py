def Sc(n):
    
    if (n > 0):

        Sc(n - 1)

    if (n % 3 == 0):

        print("Bar ")

    else:

        print(n , " Foo")
    
n = input()

Sc(int(n))