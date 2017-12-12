# HACKERRANK: python > collection > collection.Counter

from collections import Counter

input("faltu input")

shoeSize = map(int ,input().split())

counter_element = Counter(shoeSize)

total_price = 0

for _ in range(int(input())):

	size,price = map(int,input().split())

	if counter_element[size] > 0:
		total_price += price
		counter_element[size] -= 1

print(total_price)		



