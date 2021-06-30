'''mriganka_sort(arg) is my own sorting function which accept
one argument as a list and return it's sorted list.'''

def mriganka_sort(b):
    c = len(b)
    e = 0
    d = True
    while int(d) == 1:
        for i in range(c - 1):
            if b[i] > b[i + 1]:
                b[i], b[i + 1] = b[i + 1], b[i]
                e += 1
            if e == 0:
                d = False
            e = 0
    return b
c = [2, 1, 4, 7, 9, 11, 3]
print(mriganka_sort(c))
