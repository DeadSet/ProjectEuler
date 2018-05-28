def is_prime(x):
    factor_count = 0
    for i in range(1,x+1):
        if x % i == 0:
            factor_count += 1
    if factor_count == 2:
        return True
    return False

def largest_prime_factor(x):
    for i in range(x,1,-1):
        if x % i == 0 and is_prime(i):
            return i
        print(i)
    

print(largest_prime_factor(60086008514751435147))