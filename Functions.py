def createMat(x,y):
    res = []

    for i in range(0,y):
        res.append([])

    for i in res:
        for j in range(0,x):
            i.append(0)

    return res

def calcDis(x1,y1,x2,y2):

    res= (((x2-x1)**2)+((y2-y1)**2))**(1/2)

    return res
