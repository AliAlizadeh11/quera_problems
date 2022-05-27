from operator import le
from traceback import print_tb


n = input().split()

while True:
    a = sum(n)
    if len(str(a)) == 1:
        break
print(a)