n = int(input())
k = int(input())
a = []
b = []
minimum = 999999
maximum = 0
for i in range(n):
    c, d = input().split()
    a.append(int(c))
    b.append(int(d))
    minimum = min(minimum, min(a[i], b[i]))
    maximum = max(maximum, max(a[i], b[i]))

sred = (maximum - minimum) / 2
minimum = 0
our_k = 0

while round(minimum, 2)  != round(maximum, 2):
    k_max = 0
    for i in range(n):
        k_max += (a[i] // sred) * (b[i] // sred)
        our_k = sred

    if k_max > k:
        minimum = sred
        sred = (maximum + minimum) / 2
    elif k_max < k:
        maximum = sred
        sred = (maximum + minimum) / 2
    else:
        our_k = sred
        minimum = sred
        sred = (maximum + minimum) / 2


print(round(our_k, 2))




