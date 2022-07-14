# import time

# # ctime = time.time()
# a = time.perf_counter()
# n = input()
# # stime = time.time()
# b = time.perf_counter()
# if b - a < 0.4:
#     print('quera!')

import sys, select

# print "You have ten seconds to answer!"

i, o, e = select.select( [sys.stdin], [], [], 0.5 )

if (i):
#   print "You said", sys.stdin.readline().strip()
    print('quera!')
# else:
#   print "You said nothing!"