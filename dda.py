import matplotlib.pyplot as plt
def mkp(x):
    if (x*10)%10 >= 5:
        px=int(x)+1
    else :
        px=int(x)
    return px

def showfig():
    fig, ax = plt.subplots()
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.plot(pltx,plty)
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.grid()
    plt.show()

def main():
    pltx = []
    plty = []
    sx = int(input("enter starting x "))
    sy = int(input("enter starting y "))
    ex = int(input("enter ending x "))
    ey = int(input("enter ending y "))
    x, y = sx, sy
    m = (ey-sy)/(ex-sx)
    if m <= 1:
        dx = 1
        dy = m
    elif m > 1:
        dy = 1
        dx = 1/m

    if sx > ex:
        dx = dx*-1
    if sy > ey:
        dy = dy*-1
    print("m={0:.2f} Dx = {1:.2f} Dy = {2:.2f} ".format(m,dx,dy))
    print("x\ty\t\tx plot\ty plot\t\t(x, y)")
    while x != ex and y != ey:
        px=mkp(x)
        py=mkp(y)
        pltx.append(px)
        plty.append(py)

        print("{0}\t{1:.2f}\t\t{2}\t{3}\t\t({2}, {3})".format(x,y,px,py))
        x += dx
        y += dy
    showfig()

if __name__=="__main__":
    main()
