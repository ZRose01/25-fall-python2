def is_perfect(n):
    tSum = 0
    for i in range(1 , n - 1):
        if(n % i == 0):
            tSum += i
    return (tSum == n)

def lcm(n1 , n2):
    o = 0
    numinQ = 1
    while not(o):
        if(numinQ % n1 == 0 and numinQ % n2 == 0):
            return(numinQ)
        numinQ += 1

print(is_perfect(100))
print(is_perfect(496))
print(lcm(6 , 10))
print(lcm(3 , 10))
print(lcm(10 , 30))
