f1 = 1
f2 = 1
n = int(input())
for i in range(2, n - 1):
    f1, f2 = f2, f1 + f2
    print(f2)
    p = f2
    f1, f2 = f2, f1 + f2
print(f2)
print(f2 / p)
