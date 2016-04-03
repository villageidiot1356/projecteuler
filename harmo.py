"olala"

def hdenom(p):
    b=1; n=1
    while(b%p!=0):
        n=n+1
        fac=fact(n)
        print(str(n)+"!=",fac)
        numer=sum([fac/k for k in range(1,n)])
        print("numer=",numer)
        b=fac/pgcd(numer,fac)
        n=n+1
    return b





def fact(n):
    if n==0:
        return 1
    else:
        u=1;k=1
        while (k<n):
            k=k+1
            u=k*u
        return u

def pgcd(a, b):
    while b:
        a, b = b, a%b
    return a
