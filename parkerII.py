def len(l):
    e = 0
    for i in l:
        e = e + 1
    return(e)


def sum(l):
    e = 0
    for i in l:
        e = e + i
    return(e)


def avg(l):
    return (sum(l)/len(l))
