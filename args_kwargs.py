""" *args used to pass multiple argument
    **kwargs is used to pass arguments of key value pair"""

def argv(first, *args):
    """ First argument is taken by first rest all go to *args"""

    print("FIRST ARGUMENT IS :", first)
    print("REST ARGUMENT ARE of TYPE:", type(args))

    for x in args:
        print(x)


def kargv(**kwargs):
    """ kwargs are of  Dictionaries type"""

    print("TYPE OF **KWARGS :", type(kwargs))

    for key, value in kwargs.items():

        print("{0}={1}".format(key, value))


import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())


if __name__ == "__main__":
    argv(3, 'aneesh', 5,'jain',77)

    kargv(name='aneesh', srname='jain', rollno='16ucs036', value=11400540)

    dictionaries = {'ubuntu': 'LINUX', 'windows': 10}
    kargv(**dictionaries)
