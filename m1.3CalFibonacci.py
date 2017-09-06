# 斐波那契数列(Fibonacci Sequence)  
a, b = 0, 1
while a < 1000:
    print(a, end = ',')
    a, b = b, a + b
