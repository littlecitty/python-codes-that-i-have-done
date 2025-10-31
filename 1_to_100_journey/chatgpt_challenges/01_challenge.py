#finding all armstrong numbers from 1 to 10000.

for i in range(1, 10000):
    f=i
    count = len(str(i))
    d=0
    while i > 0:
        c = i % 10
        d += c ** count
        i = i // 10
    if f == d:
        print(f)
