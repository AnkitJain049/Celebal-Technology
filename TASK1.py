def upper_triangular(n):
    for i in range(n, 0, -1):
        print('* ' * i)

def lower_triangular(n):
    for i in range(1, n + 1):
        print('* ' * i)

n = 5
lower_triangular(n)
upper_triangular(n)
