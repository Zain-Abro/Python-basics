a = 0
b = 1

for i in range(1, 10000):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
