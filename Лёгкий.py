def f(x):
    d = set()
    for i in range(2, int(x**0.5+1)):
        if x % i == 0:
            d |= {i, x // i}
    if len(d) > 0:
        return 0
    else:
        return 1
    
line = open('9_17522.csv')
k = 0

for line in line:
    a = [int(x) for x in line[:-1].split(';')]
    a.sort()
    if sum(list(map(lambda x: f(x), a))) > 0 or \
    (a[0] + a[-1]) == (a[1] + a[2]):
        k += 1
print(k)

    
