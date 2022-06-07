from multiprocessing import Condition
from re import A


x, y = map(int,input().split())
r = int(input())
dx, dy = map(int,input().split())

a = dx >= x and dx <= x + r
b = dy >= y - r and dy <= y

if a and b:
    print("Mahdi")
else:
    print("Parsa")