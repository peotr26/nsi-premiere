# Chapître 2 : Ecriture d'un entier naturel en base b, avec b $\geq$ 2

## Introduction

Nous utilisons, dans la vie courante, le sytème décimal. Noud contons en base 10. Nous utiliusons la numeration positionnelle.

Eg//  
$36_{10} = 3 \times 10 ^{1} + 6 \times 10 ^{0}$  
$306_{10} = 3 \times 10 ^{2} + 0 \times 10 ^{1} + 6 \times 10 ^{0}$  

$8_{10} = 8 \times 10 ^{0}$  
$8_{10} = 8$

Eg// Travaillons en base 2  
Nous avons deux symboles : 0 et 1.  

$10_2 = 1 \times 2^1 + 0 \times 2^0$  
$10_2 = 2$

$110111_2 = 1 \times 2^5 + 1 \times 2^4 + 0 \times 2^3 + 1 \times 2^2 + 1 \times 2^1 + 1 \times 2^0$  
$110111_2 =32 +16 + 0 +4 + 2 +1$  
$110111_2 = 55$

Eg// Travaillons en base 5  
Nous avons 5 symboles : 0, 1, 2, 3, 4.

$12_5 = 1 \times 5^1 + 2 \times 5^0$  
$12_5 = 5 + 2$  
$12_5 = 7$

Eg// Travaillons ene base 16  
Nous avons 16 symboles : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B , C, D, E, F.

$17B_{16} = 1 \times 16^2 + 7 \times 16^1 + 11 \times 16^1$  
$17B_{16} = 256 + 112 + 11$  
$17B_{16} = 379$

Définition :

On considère b un entier naturel supérieur ou égal à 2. Un entier naturel s'écrit, dans une numération positionnelle : ${a_n a_{n-1} ... a_1 a_0}_b$  
$a_n, a_{n-1}, ..., a_0$ sont des des symboles scpécifiques en base b. Il y a b symboles scpécifiques en base b.  
${a_n a_{n-1} ... a_1 a_0}_b = a_n \times b^n + a_{n-1} \times b^{n-1} + ... + a_1 \times b^1 + a_0 \times b^0$  
$= \sum_{n}^{i=0} a_i \times b^1$

>Remarques :  
>- $a_n$ se lit "a indice n".  
>- $\Sigma$ correspont à sigma qui vient du grand *S* de somme.
>- $\sum_{5}^{i=0}i^2 = 0^2 + 1^2 + 2^2 + 3^2 + 4^2 + 5^2$

Eg//

$\underline{102D}_{14}$

Ecrire en base 10.

$= 1 \times 14^3 + 0 \times 14^2 + 2 \times 14^1 + 13 \times 14^0$  
$= 2744 + 28 + 13$  
$=\underline{2785}$

## Passage de la base 10 à la base 2

**Eg//** écrire 37 en base 2.

Première méthode : La méthode des soustrations succesives

$37 - 32 = 5$  
$37 = 2^5 +5$  
$5-4 = 1$  
$37 = 2^5 + 2^2 + 2^0$  
$37 = \underline{100101}_2$  

`bin(37)`vous renvoie "ob100101"

Deuxième méthode : La méthode des divisions euclidiennes successives. (ici c'est par 2).

Voir cahier de brouillon.

>**Propriété 1 :** (admise)  
Soit `b` un entier naturel supérieur ou égal à 2.  
Il y a deux méthodes pour passer de la base 10 à la base `b` : 
>- **La méthode des soustractions succesives** par les plus grandes puissances de `b` possibles. On s'arrête quand la différence est nulle.
>- **La méthode des divisions euclidiennes succesives** par `b`. On s'arrête quand le quotient est nul. Le résultat en base 10 s'obtient en prenant les rsetes à "l'envers".  

## Passage de la base 10 à la base 16

**Eg//** une couleur peut être codée par la synthèse de 3 couleurs : Rouge, Vert et Bleu. C'est le code RGB ; on donne 3 nombres.  

Pour le rouge : en base 10 (255, 0, 0), en base 16 (FF, 0, 0) ($255 = \underline{FF}_{16}$).  
Sous turtle: "lightblue" ou #0000AB

Soit la couleur suivante: (58, 76, 220)

1. Par la méthode des soustrations succesives, écrire 58 et 76 en base 16.
    - 58 = 16 + 42
    - 58 = 16 + 16 + 26
    - 58 = 16 + 16 + 16 + 10
    - $58 = 3 \times 16 + 10$
    - $58 = 3 \times 16^1 + 10 \times 16^0$
    - $58 = \underline{3A}_{16}$  
__
    - 76 = 16 + 60
    - 76 = 16 + 16 + 44
    - 76 = 16 + 16 + 16 + 28
    - 76 = 16 + 16 + 16 + 16 + 12
    - $76 = 4 \times 16^1 + 12 \times 16^0$
    - $76 = \underline{4C}_{16}$

1. Par la méthode des divisions succesives, écrire 220 en base 16.
    - voir feuille d'exercice
    - $220 = \underline{DC}_{16}$