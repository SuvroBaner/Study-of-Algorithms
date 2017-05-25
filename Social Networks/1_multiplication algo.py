# Naive multiplication-
def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

print(naive(100, 3))

def time_naive(a):
    return 2*a + 3  # time is linear in a

print(time_naive(100))

# Russian Peasants Algorithm-

def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z

print(russian(57, 86))

# The time for Russian is log base 2 a

# Divide and Conquer

def rec_russian(a, b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2*rec_russian(a/2, b)
    return b + 2*rec_russian((a - 1)/2, b) # take one b out, then a => a-1 becomes even, calling the subroutine

print(rec_russian(10, 12))
