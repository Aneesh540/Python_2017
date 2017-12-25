for _ in range(int(input())):

    number, min_delecious = map(int, input().split())
    l = []


    for i in range(number):
        x, deleciousness, cost = input().split()
        l.append((int(deleciousness),int(cost)))


    l.sort()

    total_cost = 0
    for i in l:

        if
