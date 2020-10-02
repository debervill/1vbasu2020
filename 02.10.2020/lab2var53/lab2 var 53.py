import math

k = 1
m = 2
c = 3

x1 = m ** 2 - k ** 2 - 4 * m * c

if x1 >= 0:
    x2 = math.sqrt(x1)
else:
    x2 = math.fabs(x1)

x1 = 12
x2 = 12

if x1 == x2:
    print("Числа равны, максимального нет")
    xmax = None
elif x1  > x2:
    xmax = x1
else:
    xmax = x2

print("X1 = " + str(x1))
print("X2 = " + str(x2))
print("Xmax = " + str(xmax))

