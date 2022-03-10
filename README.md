# Evaluation Python B1 10 Mars 2022 (from @JBienvenu)

## Rendu

Ecrivez dans un ou plusieurs fichiers python la solution aux exercices ci-dessous.
Envoyez votre rendu final sur la plateforme de l'école. Il est possible de travailler par groupe de 2.

## Exercice 1

Ecrire une fonction "carre" qui prendra en paramètre un entier "x" et retournera son carré.

```
Nom de la fonction: carre
paremètre 1: x (int)
valeur de retour: la valeur de x au carré

Exemples:
carre(5) -> 25
carre(-2) -> 4
carre(0) -> 0
```

## Exercice 2

Ecrire une fonction "bissesxtile" qui prendra en paramètre une année et retournera Vrai si cette dernière est bissextile, Faux sinon.
Pour information: Une année est bissextile si elle respecte l'un des deux critères suivants:
 - l'année est divisible par 4 et non divisible par 100
 - l'année est divisible par 400

```
Nom de la fonction: bissextile
paramètre 1: annee (int)
valeur de retour: True si 'annee' est bissextile, False sinon

Exemples:
bissextile(1900) -> False
bissextile(1936) -> True
bissextile(1992) -> True
bissextile(2005) -> False
```

## Exercice 3

Ecrire une fonction "somme_entiers" qui prend en paramètre un entier "n" et qui va retourner la somme de tout les entiers naturels jusqu'à "n"

**Bonus**: Résoudre cet exercice SANS utiliser la moindre boucle (while, for etc)
```
Nom de la fonction: somme_entiers
paremètre 1: n (int)
valeur de retour: La somme de tous les entiers naturels jusqu'à n

Exemples:
somme_entiers(10) -> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
somme_entiers(26) -> 351
somme_entiers(4) -> 10
somme_entiers(120) -> 7260
```

## Exercice 4

Ecrire une fonction "maximum_dans_liste" qui prend en paramètre une liste d'entiers et va renvoyer l'entier maximum présent dans cette liste.

```
Nom de la fonction: maximum_dans_liste
paramètre 1: entiers (list[int])
valeur de retour: Le maximum dans la liste "entiers"
Contraintes: Il est interdit d'utiliser la fonction max() de python ❌❌

Exemples:
maximum_dans_liste([1, 5, -7, 145, -200]) -> 145
maximum_dans_liste([-677, -54, -289, -439]) -> -52
```

## Exercice 5

Ecrire une fonction "compter_nombre_digits" qui prend en paramètre un entier "n" et qui retourne le nombre de chiffres qui le compose.

**Bonus**: Résoure cet exercice SANS utiliser la moindre boucle, à l'aide de la fonction log10() https://docs.python.org/3/library/math.html#math.log10

```
Nom de la fonction: compter_nombre_digits
paramètre 1: n (int)
valeur de retour: Le nombre de chiffres qui composent 'n'
contraintes: Il est interdit de transformer n en string afin de calculer la longueur de la chaine !

Exemples:
compter_nombre_digits(5) -> 1
compter_nombre_digits(8) -> 1
compter_nombre_digits(17) -> 2
compter_nombre_digits(0) -> 1
compter_nombre_digits(167876) -> 6
```

## Exercice 6

Ecrire une fonction "inverser_liste" qui va renverser une liste d'entiers passée en paramètres.

**Bonus**: Résoudre cet exercice SANS utiliser une seconde liste pour stocker le résultat.
```
Nom de la fonction: inverser_liste
paramètre 1: entiers (list[int])
valeur de retour: L'inverse de la liste "entiers"
contraintes: Il est interdit d'utiliser la fonction reversed() ou list.reverse()

Exemples:
inverser_liste([1, 6, 7, 4]) -> [4, 7, 6, 1]
inverser_liste([0, 0, 0]) -> [0, 0, 0]
inverser_liste([10, -5, 24]) -> [24, -5, 10]
```

## Exercice 7

Ecrire une fonction "decaler_zeros" qui prendra en paramètre une liste d'entiers et qui va décaler tout les zéros à la fin de la liste avant de la retourner.

**Bonus**: Résoudre cet exercice SANS utiliser une seconde liste pour stocker le résultat.

```
Nom de la fonction: decaler_zeros
paramètre 1: entiers (list[int])
valeur de retour: La liste "entiers" avec tout les zéros décalés à la fin

Exemples:
decaler_zeros([15, 0, 54, 78, -5, 0, 9]) -> [15, 54, 78, -5, 9, 0, 0]
decaler_zeros([0, 0, 0, 1, 6, -7]) -> [1, 6, -7, 0, 0, 0]
decaler_zeros([1, 7, 4]) -> [1, 7, 4]
decaler_zeros([0, 0, 0]) -> [0, 0, 0]
```

## Exercice 8

Ecrire une fonction "factorial" qui prend en paramètre un entier "n" et qui va renvoyer la factorielle de n.
Pour rappel, n! = 1 * 2 * ... * n - 1 * n
Par exemple, 5! = 1 * 2 * 3 * 4 * 5

**Bonus**: Résoudre cet exercice de deux manières différentes. Avec une récursion ET sans récursion
```
Nom de la fonction: factorial
paramètre 1: n (int)
valeur de retour: La factorielle de n
contraintes: Il est interdit d'utiliser la fonction factorial() de python https://docs.python.org/3/library/math.html#math.factorial

Exemples:
factorial(5) = 120
factorial(30) = 265252859812191058636308480000000
factorial(8) = 40320
factorial(0) = 1
factorial(1) = 1
```

## Exercice 9

Ecrire une fonction "est_premier" qui prend en paramètre un entier "n" et qui va renvoyer True si n est premier, False sinon
Pour rappel: Un nombre premier doit posséder uniquement deux diviseurs, 1 et lui même.

https://oeis.org/A000040

```
Nom de la fonction: est_premier
paramètre 1: n (int)
valeur de retour: True si n est premier, False sinon

Exemples:
est_premier(1) -> False
est_premier(2) -> True
est_premier(3) -> True
est_premier(5) -> True
est_premier(6) -> False
est_premier(241) -> True
```

## Exercice 10

Soit 'chaine' une chaine de caractères qui ne contiendra QUE les caractères '(' et ')', écrire une fonction qui va renvoyer 'True' si la chaine est valide, 'False' Sinon.
Une chaine valide est une suite de parenthèse correctements ouvertes et fermées.

**Bonus**: Résoudre cet exercice en prenant en compte les caractères suivants en plus des parenthèses : '[', ']', '{', '}'

```
Nom de la fonction: valid_parenthesis
paramètre 1: chaine (str)
valeur de retour: True si "chaine" est une séquence de parenthèses valide, False sinon

Exemples:
valid_parenthesis("()()()") -> True
valid_parenthesis("()") -> True
valid_parenthesis("((()))()") -> True
valid_parenthesis("()((") -> False
valid_parenthesis("(())()))") -> False
valid_parenthesis("(()()") -> False
```

## Exercice 11

Ecrire une fonction "tri_bulles" qui va implémenter un tri à bulles pour trier une liste d'entiers.
https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles

**Bonus**: Résoudre l'exercice en triant la liste dans l'ordre décroissant plutôt que croissant

```
Nom de la fonction: tri_bulles
paramètre 1: entiers (list[int])
valeur de retour: La liste entiers triée dans l'ordre croissant
contraintes: Il est interdit d'utiliser la fonction sorted() ou list.sort() de python

Exemples:
tri_bulles([67, 7, 34, 10, 4]) -> [4, 7, 10, 34, 67]
tri_bulles([1, 4, 7, 10]) -> [1, 4, 7, 10]
tri_bulles([1, 1, 1, 1]) -> [1, 1, 1, 1]
tri_bulles([10, 9, 8, 7, 5]) -> [5, 7, 8, 9, 10]
```

## Exercice 12

Vous devez monter un escalier à 'n' marches. A chaque étape, vous pouvez soit monter '1' ou '2' marches.
De combien de manières distinctes pouvez-vous monter cet escalier ?
Par exemple:
- Pour 2 marches, il existe 2 solutions:
  - 1 marche + 1 marche
  - 2 marches.
- Pour 3 marches, il existe 3 solutions:
  - 1 marche + 1 marche + 1 marche
  - 2 marches + 1 marche
  - 1 marche + 2 marches

Ecrire une fonction climbing_stairs qui prend en paramètre en entier "n" qui représente le nombre de marche, et qui va retourenr le nombre de manières distinctes pour gravir l'escalier.

**Bonus**: Faire en sorte que votre algorithme fonctionne pour n >= 45

```
Nom de la fonction: climbing_stairs
paramètre 1: n (int)
valeur de retour: Le nombre de combinaisons pour monter l'escalier

Exemples:
climbing_stairs(3) -> 3
climbing_stairs(6) -> 13
climbing_stairs(26) -> 196_418
climbing_stairs(45) -> 1_836_311_903
```
