""" Generators are iterator and you can iterate only once through them
    They do not reserve space in memory, they do not return a value they yield it"""

def generator_func(n,m=0):
    for i in range(m,n):
        yield i


def check_fibonacci(n):
    """ Checking if a number is fibonacci or not"""
    a,b=1,1

    while(n>0):
        a,b=b,a+b
        if b is n:
            return True

        elif b > n:
            return False

        else:
            pass


def generate_fibonacci(n):
    """ generate a nth fibonacci number"""

    if n<0:
        print("NOT POSSIBLE")
        return None

    elif 0<n<3:
        return 1

    else:
        a,b=1,1

        for j in range(n):
            a,b = b, a+b
            return b




print(generate_fibonacci(5))

print(check_fibonacci(3))
print(check_fibonacci(8))
print(check_fibonacci(7))



foo = generator_func(11)

print(foo)
print(*foo,sep=" ")
