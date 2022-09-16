# Chapître 1 : Programmation en Python

Guido van Rossen a crée le langage Python en 1989. C'est un langage haut-niveau avec un typage dynamique.

## I. Les opérations de base

`**` correspont à une puissance.  
`2**3` renvoie `8`

`sqrt(a)` renvoie la racine carré de `a`.  

`//` renvoie le coetient de la division euclidienne.  
`%` renvoie le reste de la division euclidienne.
___
>**Remarque**  
`a` est paire <=> `a%2==0`.  
`==` est un booléen.
___

## II. Affectation de variables

`a <- 2` se lit a prend la valeur 2.  

En Python, on écrit : `a=2`.

## III. Structures conditionelles

```python
if cond:
    bloc1
```

```python
if cond:
    bloc1
else:
    bloc2
```

```python
if cond1:
    bloc1
elif cond2:
    bloc2
else:
    bloc3
```

## IV. Les fonctions

en Python :

```python
def nom_variable(argument):
    bloc1
```

___
>**Remarque**  
Une variable crée à l'intérieure de la fonction est appellée une variable locale.
___

## V. Boucles bornées

En pseudocode, on écrit :

```pseudocode
Pour i variant de 1 à 4:
    Afficher i
```

En Python :

```python
for i in range(1,5):
    print(i)
```

```python
for i in range(0,10):
    bloc1
```

>Le bloc sera répété 10 fois, i prend les valeurs de 0 à 9 inclus (de 1 en 1).
___
>**Remarque**  

```python
for i in range(4,9,3):
```

>i=4
i=7
i change donc de 3 en 3.

```python
for i in range(15,3,-1):
```

>i=15  
i=...  
i=4  
i va à reculons.
___

## VI. Boucles non-bornées

En pseudocode:

```pseudocode
tant que cond:
    bloc d'instruction
```

>Ce bloc sera executé tant que la condition de départ est vraie.

En Python :

```python
while cond:
    bloc1
```
