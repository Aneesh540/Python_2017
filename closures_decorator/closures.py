# Defining function from within functions

def hii(name="aneesh"):
    print("You r inside hii, u are inside hii()")

    def hlo():
        return "seentex code 917, u r inside hlo()"

    def unse():
        return "You are inside une()"

    if name is 'aneesh':
        return hlo

    else:
        return unse


a = hii()
print(a)
print(a())

b = hii
del hii

try:
    print(hii())
    print("printing hii")

except NameError:
    print("printing b coz hii() is deleted")
    print(b)

print('\n'*10)


# Giving function as argument to a another function

def hi():
    return "Hlo LDrago!"


def someBoringStuff(func):
    print("doing some boring stuff before function.__name__ == {}".format(func.__name__))
    func()

someBoringStuff(hi)
