def carre(x):
    return x**2

def bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0):
        return True
    elif (annee % 400 == 0):
        return True
    else:
        return False

def somme_entiers(n):
    for i in range(n):
        n = n + i
    return n


if __name__ == "__main__":
    assert(carre(5) == 25)
    assert(carre(-2) == 4)
    assert(carre(0) == 0)
    print("Fonction carre validée ! ✔")
    
    assert(bissextile(1900) == False)
    assert(bissextile(1936) == True)
    assert(bissextile(1992) == True)
    assert(bissextile(2005) == False)
    print("Fonction bissextile validée ! ✔")
    
    assert(somme_entiers(10) == 55)
    assert(somme_entiers(26) == 351)
    assert(somme_entiers(4) == 10)
    assert(somme_entiers(120) == 7260)
    print("Fonction somme_entiers validée ! ✔")