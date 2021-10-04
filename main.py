import datetime
def get_largest_prime_below(n):
    '''
    Functia returneaza ultimul numar prim mai mic decat n
    :param n: n, k, ok, i
    :return: returneaza in k ultimul numar prim
    '''
    k=0
    while k==0:
        ok=True
        n=n-1
        for i in range(2,n//2+1):
            if n%i==0:
                ok=False
        if ok:
            k=n
    return k

def test_get_largest_prime_below():
    assert(get_largest_prime_below(6))==5
    assert (get_largest_prime_below(10)) == 9

def get_age_in_days(birthday):
    m=birthday[0:2]
    p=birthday[4:6]
    q=birthday[8:12]
    zile_total=0
    for i in range(q,2021):
        if i%4==0:
            zile_total=zile_total+366
        else:
            zile_total=zile_total+365

def main():
    while True:
        print("1.Gaseste ultimul numar prim, mai mic decat cel dat.")
        print("2.Calculeaza varsta unei persoane in zile.")
        print("x.Iesire")
        optiune=input("Dati optiunea:")
        if optiune=='x':
            break
        elif optiune=='1':
            nr=int(input("Dati numarul:"))
            if nr < 3:
                print("Nu este o valoare valida.Reincercati.")
            else:
                maxnr=get_largest_prime_below(nr)
                print(f"Ultimul numar prim mai mic decat {nr} este: {maxnr}")
        elif optiune=='2':
            birthday=input("Introduceti data nasterii (YYYY/MM/DD): ")
            print(get_age_in_days(birthday))

    test_get_largest_prime_below()
main()