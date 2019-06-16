# program to display magic square for odd order
n = int(input("enter the order: "))

sum = n * ((n ** 2) + 1) / 2

print("the magic number is %d" % sum)

a = [[0 for x in range(n)] for y in range(n)]

i = n // 2
j = n - 1

num = 1
while num <= (n * n):
    if i == -1 and j == n:  # 3rd condition
        j = n - 2
        i = 0
    else:
        if j == n:
            j = 0

        if i < 0:
            i = n - 1

    if (a[i][j] != 0):  # 2nd condition
        j = j - 2
        i = i + 1
        continue
    else:
        a[i][j] = num
        num = num + 1

    j = j + 1
    i = i - 1  # 1st condition

print("Magic Square for n =", n)

for i in range(0, n):
    for j in range(0, n):
        print('%d ' % (a[i][j]), end='')

        if j == n - 1:
            print()
