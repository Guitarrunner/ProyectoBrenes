def createMat(x,y):
    res = []

    for i in range(0,y):
        res.append([])

    for i in res:
        for j in range(0,x):
            i.append(0)

    return res
