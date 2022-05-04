def my_reverse(l):
    i = len(l)
    k = 0
    new_list = [None] * i
    while (i > 0):
        new_list[k] = l[i - 1]
        i -= 1
        k += 1
    print(new_list)


