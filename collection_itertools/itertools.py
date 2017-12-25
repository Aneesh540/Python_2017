"""
itertools.product( *iterables, repeat = 1)
itertools.permutations(iterable,r = None)
"""

import itertools

def main():

    Product()





def Product():
    """ Returns a cartesian product"""

    x = itertools.product([1,2,3], ['a','b','c'])
    print(*x)
    # (1, 'a')(1, 'b')(1, 'c')(2, 'a')(2, 'b')(2, 'c')(3, 'a')(3, 'b')(3, 'c')

    x = itertools.product([1,2,3],repeat=2)
    print(*x)
    # (1, 1)(1, 2)(1, 3)(2, 1)(2, 2)(2, 3)(3, 1)(3, 2)(3, 3)

    x = itertools.product(range(2),repeat=3)
    print(*x,sep='\n')
    # all 8 combinations of 0/1


    print('*'*50,'\n')


def Permutation():
    """ Returns """
    pass



if __name__ == "__main__" :
    main()