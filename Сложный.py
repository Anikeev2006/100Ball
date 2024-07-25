def f(n):
    while n > 9:
        t = 0
        while n > 0:
            t += n % 10
            n //= 10
        n = t
    return n

line = open('9_17522.csv')
k = 0

for line in line:
    a = [int(x) for x in line[:-1].split(';')]
    a = list(map(lambda x: f(x), a))
    
    npovt = [int(x) for x in a if a.count(x) == 1]
    if 5 in a and len(npovt) == 4:
        k += 1
print(k)
