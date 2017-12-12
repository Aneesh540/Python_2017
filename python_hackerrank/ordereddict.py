# HACKERRANK: PYTHON > COLLECTION >

from collections import OrderedDict
audi = OrderedDict()

testing = OrderedDict()
testing['aneesh'] = 2
testing['ldrago'] = 45
testing['L'] = 11

for key, value in testing.items():
    print(key, '->', value)

x = int(input())

for _ in range(x):

    key, space, value = input().rpartition(' ')
    # str.rpartition(" ")  divide the string into 3 parts
    # >>> "aneesh jain is Ldrago".rpartition(" ")
    # >>> ('aneesh jain is', ' ', 'ldrago')

    if key in audi.keys():
        audi[key] += int(value)

    else:
        audi[key] = int(value)

for i in audi:
    print(i, audi[i])
