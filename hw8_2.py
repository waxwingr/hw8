def dividers(x):
    sup = range(1, (x + 1))
    out = []
    for num in sup:
        if x % num == 0:
            out.append(num)
    return (out)
