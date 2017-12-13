# HACKERRANK: PYTHON > COLLECTIONS > WordOrder

from collections import OrderedDict

od = OrderedDict()

for _ in range(int(input())):
    x = input()

    if x in od:
        od[x] += 1

    else:
        od[x] = 1

print(len(od.keys()))
print(*od.values())
