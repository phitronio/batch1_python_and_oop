import time
from functools import cache
# 1, 1, 2, 3, 5, 8, 13, 21---

@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

start = time.time()

for i in range(37):
    print(i, fib(i))

end = time.time()
mili_seconds = (end-start)*1000
print( 'Time took', mili_seconds)

# without cache
# Time took 6734.106063842773