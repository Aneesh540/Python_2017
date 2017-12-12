from collections import namedtuple

test_cases = int(input())
total = 0

Student = namedtuple('Student', input())

for _ in range(test_cases):
    A, B, C, D = input().split()
    total += float(Student(A, B, C, D).MARKS)

print(total / test_cases)
