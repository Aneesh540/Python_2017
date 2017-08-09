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
        return "NOT POSSIBLE"

    elif 0<n<3:
        return 1

    else:
        a,b=1,1

        for j in range(n-2):
            a,b = b, a+b

        return b


def yield_fibonacci(n):
    """ yield upto nth fibonacci number"""
    a, b = 1, 1

    for _ in range(n):
        yield a
        a,b = b,a+b



if __name__ == "__main__":

    foo = generator_func(11)

    print(foo)
    print(*foo,sep="\t")

    r = int(input("no.upto which u want to generate fibonacci number:"))
    print(*yield_fibonacci(r),sep='\t')

    print(generate_fibonacci(100))

    print(check_fibonacci(99))
    print(check_fibonacci(8))
    print(check_fibonacci(7))
