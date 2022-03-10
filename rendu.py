from math import log10
from pydoc import cli
## Exercice 1
def carre(x):
    return x**2

## Exercice 2
def bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0):
        return True
    elif (annee % 400 == 0):
        return True
    else:
        return False

## BONUS - Exercice 3
def somme_entiers(n):
    if n == 0:
        return 0
    else:
        return n + somme_entiers(n - 1)

## Exercice 4
def maximum_dans_liste(entiers):
    for i in range(len(entiers)):
        if (entiers[i] > entiers[0]):
            temp = entiers[0]
            entiers[0] = entiers[i]
            entiers[i] = temp
    return entiers[0]

## Exercice 5
def compter_nombre_digits(n):
    n = abs(n)
    if n > 0:
        digits = int(log10(n)) + 1
    elif n == 0:
        digits = 1
    return digits

## Exercice 6
def inverser_liste(entiers):
    for i in range((len(entiers) // 2)):
        temp = entiers[i]
        entiers[i] = entiers[(len(entiers) -1) - i]
        entiers[(len(entiers) -1) - i] = temp
    return entiers

## Exercice 7
def decaler_zeros(entiers):
    """
    Ecrire la fonction decaler_zeros, qui prend en entrée une liste d'entiers n, et qui déplacera tout les 0 à la fin de la liste avant de la renvoyer.
    Exemple: Pour liste = [45, 0, 7, 12, 98, 0, 0, 1, 54], la fonction doit renvoyer [45, 7, 12, 98, 1, 54, 0, 0, 0]
    """
    # Ecrire votre code ici
    i = 0 
    count = 0
    while (i < len(entiers)):  
        if entiers[i] == 0 and entiers[(len(entiers) -1) - count] != 0:
            entiers.append(entiers[i])
            entiers.pop(i)
            count+=1
            i-=1
        i+=1   
    return entiers

## Exercice 8 - Sans récursion
def factorial(n):
        if n == 0:
            return 1
        else:
            fact = 1
            for k in range(2,n+1):
                fact = fact * k
            return fact
## Exercice 8 - Avec récursion
def rec_factorial(n):
    if n == 0:
        return 1
    else:
        return n  * factorial(n-1)


## Exercice 9
def est_premier(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
         if (n % i) == 0:
            return False
        else:
            return True
    else:
        return False

## Exercice 10
def valid_parenthesis(chaine): 
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 
    count = 0
    check = 0
    for i in range(len(chaine)):
        if chaine[i] in open_list:
            count +=1
            check += 1
        elif (chaine[i] in close_list) and (check > 0):
            count+=1
            check-=1
    if count == len(chaine) and check == 0:
        return True
    else:
        return False

## Exercice 11
def tri_bulles(entiers):
    for i in range(len(entiers)-1):
        for j in range(0, len(entiers)-i-1):
            if entiers[j] > entiers[j + 1] :
                entiers[j], entiers[j + 1] = entiers[j + 1], entiers[j]
    return entiers

def rev_tri_bulles(entiers):
    for i in range(len(entiers)-1):
        for j in range(0, len(entiers)-i-1):
            if entiers[j] < entiers[j + 1] :
                entiers[j], entiers[j + 1] = entiers[j + 1], entiers[j]
    return entiers

## Exercice 12
def climbing_stairs(n):
    if n == 1 or n == 2:
        return n
    v1 = 1
    v2 = 2
    marches = 0
    for pas in range(3, n+1):
            marches = v1 + v2
            v1 = v2
            v2 = marches

    return marches


if __name__ == "__main__":
    ## Check] Exercice 1  
    assert(carre(5) == 25)
    assert(carre(-2) == 4)
    assert(carre(0) == 0)
    print("Exercice 1 - carre validée ! ✔")
    
    ## Check] Exercice 2
    assert(bissextile(1900) == False)
    assert(bissextile(1936) == True)
    assert(bissextile(1992) == True)
    assert(bissextile(2005) == False)
    print("Exercice 2 - bissextile validée ! ✔")
    
    ## Check] Exercice 3+BONUS
    assert(somme_entiers(10) == 55)
    assert(somme_entiers(26) == 351)
    assert(somme_entiers(4) == 10)
    assert(somme_entiers(120) == 7260)
    print("Exercice 3+BONUS - somme_entiers validée ! 🎉")
    
    
    assert(maximum_dans_liste([1, 5, -7, 145, -200]) == 145)
    assert(maximum_dans_liste([-677, -54, -289, -439]) == -54)
    print("Exercice 4 - maximum_dans_liste validée ! ✔")
    
    ## Check] Exercice 5+BONUS
    assert(compter_nombre_digits(5) == 1)
    assert(compter_nombre_digits(8) == 1)
    assert(compter_nombre_digits(17) == 2)
    assert(compter_nombre_digits(0) == 1)
    assert(compter_nombre_digits(167876) == 6)
    print("Exercice 5+BONUS - compter_nombre_digits validée ! 🎉")

    ## Check] Exercice 6+BONUS
    assert(inverser_liste([1, 6, 7, 4]) == [4, 7, 6, 1])
    assert(inverser_liste([0, 0, 0]) == [0, 0, 0])
    assert(inverser_liste([10, -5, 24]) == [24, -5, 10])
    print("Exercice 6+BONUS - inverser_liste validée ! 🎉")

    ## Check] Exercice 7+BONUS
    assert(decaler_zeros([15, 0, 54, 78, -5, 0, 9]) == [15, 54, 78, -5, 9, 0, 0])
    assert(decaler_zeros([0, 0, 0, 1, 6, -7]) == [1, 6, -7, 0, 0, 0])
    assert(decaler_zeros([1, 7, 4]) == [1, 7, 4])
    assert(decaler_zeros([0, 0, 0]) == [0, 0, 0])
    print("Exercice 7+BONUS - decaler_zeros validée ! 🎉")

    ## Check] Exercice 8 - Sans récursion
    assert(factorial(5) == 120)
    assert(factorial(30) == 265252859812191058636308480000000)
    assert(factorial(8) == 40320)
    assert(factorial(0) == 1)
    assert(factorial(1) == 1)
    print("Exercice 8(sans récursion) - factorial validée ! ✔")
    ## Check] Exercice 8 - Avec récursion
    assert(rec_factorial(5) == 120)
    assert(rec_factorial(30) == 265252859812191058636308480000000)
    assert(rec_factorial(8) == 40320)
    assert(rec_factorial(0) == 1)
    assert(rec_factorial(1) == 1)
    print("Exercice 8(avec récursion) - rec_factorial validée ! 🎉")
    
    ## Check] Exercice 9
    assert(est_premier(1) == False)
    assert(est_premier(2) == True)
    assert(est_premier(3) == True)
    assert(est_premier(5) == True)
    assert(est_premier(6) == False)
    assert(est_premier(241) == True)
    print("Exercice 9 - est_pair validée ! ✔")

    ## Check] Exercice 10
    assert(valid_parenthesis("()()()") == True)
    assert(valid_parenthesis("()") == True)
    assert(valid_parenthesis("((()))()") == True)
    assert(valid_parenthesis("()((") == False)
    assert(valid_parenthesis("(())()))") == False)
    assert(valid_parenthesis("(()()") == False)
    print("Exercice 10+BONUS - valid_parenthesis validée ! ✔")

    ## Check] Exercice 11
    assert(tri_bulles([67, 7, 34, 10, 4]) == [4, 7, 10, 34, 67])
    assert(tri_bulles([1, 4, 7, 10]) == [1, 4, 7, 10])
    assert(tri_bulles([1, 1, 1, 1]) == [1, 1, 1, 1])
    assert(tri_bulles([10, 9, 8, 7, 5]) == [5, 7, 8, 9, 10])
    print("Exercice 11 - tri_bulles validée ! ✔")
    
    ## Check] Exercice 11 - Reversed
    assert(rev_tri_bulles([67, 7, 34, 10, 4]) == [67, 34, 10, 7, 4])
    assert(rev_tri_bulles([1, 4, 7, 10]) == [10, 7, 4, 1])
    assert(rev_tri_bulles([1, 1, 1, 1]) == [1, 1, 1, 1])
    assert(rev_tri_bulles([10, 9, 8, 7, 5]) == [10, 9, 8, 7, 5])
    print("Exercice 11(BONUS) - tri_bulles validée ! ✔")

    ## Exercice 12
    assert(climbing_stairs(3) == 3)
    assert(climbing_stairs(6) == 13)
    assert(climbing_stairs(26) == 196_418)
    assert(climbing_stairs(45) == 1_836_311_903)
    assert(climbing_stairs(47) == 480_7526_976)
    print("Exercice 12+BONUS - climbing_stairs validée ! ✔")