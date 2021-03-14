def nty_wyraz(a,q,n):
    print("Wybrałeś wzór na n-ty wyraz ciągu")
    wyraz = a * q**(n-1)
    print(wyraz)

def suma_nwyrazow(a,q,n):
    print("Wybrałeś wzór na sume n wyrazow ciągu")
    if q!=1:
        suma = (a * ((1 - q**n) / (1 - q)))
        print(suma)
    else:
        suma = a * n
        print(suma)

