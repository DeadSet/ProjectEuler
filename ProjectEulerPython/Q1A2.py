import time

start = time.time()

by3 = set(range(0,1000,3))
by5 = set(range(0,1000,5))

by_both = by3 | by5

print(sum(by_both))
print(time.time()-start)

