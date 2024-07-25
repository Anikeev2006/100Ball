

f = open('9_17522.csv')
l = []

for f in f:
    a = [int(x) for x in f.split(';')]
    l.append(a)
    
k = 0
for i in range(0, len(l)-1, 2):
    if l[i][2] > l[i+1][2] and \
       (sum(l[i]) / 4) > (sum(l[i+1]) / 4):
        k += 1
print(k)
