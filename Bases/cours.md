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

Eg// écrire 37 en base 2.

Première méthode : La méthode des soustrations succesives

$37 - 32 = 5$  
$37 = 2^5 +5$  
$5-4 = 1$  
$37 = 2^5 + 2^2 + 2^0$  
$37 = \underline{100101}_2$  


`bin(37)`vous renvoie "ob100101"

Deuxième méthode : La méthode des divisions euclidiennes successives. (ici c'est par 2).

Voir cahier de brouillon.