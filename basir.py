def main():
    pltx = []
    plty = []
    sx = int(input("enter starting x "))
    sy = int(input("enter starting y "))
    ex = int(input("enter ending x "))
    ey = int(input("enter ending y "))
    x, y = sx, sy
    m = (ey-sy)/(ex-sx)
    p = 0
    if m<0:
        print("I cannot do this !")
        return

    if m<1:
        p = 2 * (ey-sy) - (ex-sx)
    else :
        p = 2 * (ex-sx) - (ey-sy)
    nx=sx;
    ny=sy;
    print("K\t (Xk, Yk)\t Pk\t (Xk+1,Yk+1)")
    i=0;
    while(True):

        if(nx==ex and ny==ey):
            break;

        if p<=0 :
            if m<1:
                xk = nx+1
                yk = ny
            else:
                yk = ny+1
                xk = nx
        else:
            xk = nx+1
            yk = ny+1
        print("{0}\t ({1}, {2})\t {3}\t ({4},{5})".format(i,nx,ny,p,xk,yk))
        p = p + 2 * (ey-sy) - 2 * (ex-sx) * (yk-ny)
        nx = xk
        ny = yk
if __name__=="__main__":
    main()
