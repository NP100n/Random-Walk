def probabiliter(ip):
    lll = []
    for i in range(ip):
        lll.append(1)
    for i in range(100 - ip):
        lll.append(-1)
    return lll

def randWalk(ip):
    x = 0
    for i in range(10000):
        x += random.choice(probabiliter(ip))
    return x

def lstie(ip):
    lst = []
    for i in range(1000):
        lst.append(randWalk(ip))
    return lst


def median(ip):
    xlst = []
    y = lstie(ip)
    c = 1000
    for l in range(1000):
        k = y[0]
        for p in range(c):
            if y[p] < k:
                k = y[p]
        y.remove(k)
        xlst.append(k)
        c -= 1

    return xlst[499]
