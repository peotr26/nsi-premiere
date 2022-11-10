
#####################################
###                               ###
###   Le labyrinthe impossible    ###
###                               ###
#####################################

# Ce labyrinthe sera sûrement impossible.
# Si il fonctionne alors vous avez beaucoup de chance.

# Auteur : Pierre Fernagu--Berthier

# Importation des bibliotèques :

from turtle import *
from random import randrange


# Paramétrage de certains paramètres :

bgcolor('white')                                # Mettre le fond en couleur blanche.
speed(0)                                        # Mettre la vitesse de la tortue à 0 car sinon c'est trop lent.
ht()                                            # Cacher la tortue.


# Création des fonctions nécessaires :

def goto_am(x,y):
    '''Fonction qui permet d'aller à des coordonées precis.
    
    x -- Coordonée sur l'axe de l'ordonnée
    y -- Coordonée sur l'axe de l'abscisse
    '''
    up()
    goto(x,y)
    down()

def move(s,o):
    '''Fonction qui permet de se déplacer en fonction d'une disctance spécifiée.
    
    s -- Taille du déplacement
    o -- Orientation du déplacement
    '''
    up()
    setheading(o)
    forward(s)
    down()

def go_back(s,o):
    '''Fonction qui permet d'aller à la ligne suivante.
    
    s -- Taille du labyrinthe
    o -- Orientation du déplacement
    '''
    up()
    move(s,o+180)                               # Se déplace vers le début de la ligne.
    move(s/20,o+90)                             # Se déplace au niveau de la ligne suivante.
    down()
    
def line(s,o,colour):
    '''Fonction qui dessine une droite avec une couleur spécifiée.
    
    s -- Taile de la droite
    o -- Orientation de la droite
    colour -- Couleur de la ligne
    '''
    down()
    color(colour)
    setheading(o)
    forward(s)    

def main_structure(x,y,s):
    '''Fonction qui dessine le cadre autour du quadrillage du labyrinthe.
    
    x -- Coordonée sur l'axe de l'ordonnée
    y -- Coordonée sur l'axe de l'abscisse
    s -- Taile du labyrinthe
    '''
    goto_am(x, y)
    color('black')
    for i in range(0,4):                        # Boucle qui dessine les contours du labyrinthe.
        forward(s)
        left(90)

def opening(x,y,s,o):
    '''Fonction qui dessine une ouverture du labyrinthe en fonction de ses coordonées.
    
    x -- Coordonée sur l'axe de l'ordonnée
    y -- Coordonée sur l'axe de l'abscisse
    s -- Taile du labyrinthe
    o -- Orientation de l'ouverture
    '''
    goto_am(x,y)
    line(s/20,o,'white')                        # Dessine une ouverture du labyrinthe.
    
def choose_colour():
    '''Fonction qui choisit entre le noir et le blanc aléatoirement. Le noir a 2/3 chances d'être choisis.
    '''
    if randrange(0,3) == 0:                     # Si randrange sort 0 alors choisir la couleur blanche.
        return 'white'
    else:                                       # Sinon choisir la couleur noire.
        return 'black'
    
def serie_line(s,o):
    '''Fonction qui dessine une ligne composant le quadrillage.

    s -- Taille du labyrinthe
    o -- Orientation de la ligne
    '''
    for i in range(0,int(s/20)):                # Boucle qui va dessinée une ligne du quadrillage en fonction de la taille du labyrinthe et de façon à faire des cases de 20 sur 20.
        line(20, o, choose_colour())            # A chaque execution choisir la couleur avec la fonction choose_colour.
        
def draw_series(s):
    '''Fonction qui va dessiner le quadrillage du labyrinthe aléatoirement.
    
    s -- Taille du labyrinthe
    '''
    a = 19                                      # Variable permettant le fonctionnement la boucle suivante.
    while a != 0:                               # Boucle pour dessiner les lignes horizontales.
        serie_line(s,0)
        go_back(s,0)
        a -= 1                                  # Soustrait 1 à a à chaque iteration afin de faire fonctionner la boucle.
    move(s/20,0)
    for i in range(1,20):                       # Boucle pour dessiner les lignes verticales.
        serie_line(s,180+90)
        go_back(s,180+90)

def text(x,y):
    '''Fonction qui va écrire le texte suivant : Si le labyrinthe fonctionne, alors tu es ultra chanceux !
    
    x -- Coordonée sur l'axe de l'ordonnée.
    y -- Coordonée sur l'axe de l'abscisse.
    '''
    color('black')
    up()
    goto(x, y)
    width(15)
    write('Si le labyrinthe fonctionne, alors tu es ultra chanceux !',align='center',font=('times new roman',20,'bold'))

def display():
    '''Fonction qui va effectuer l'affichage du programme.
    '''
    up()
    goto(-200,-180)
    draw_series(400)                            # Création du quadrillage.
    main_structure(-200,-200,400)               # Création du contour du labyrinthe.
    opening(-200,-200,400,0)                    # Création de la première ouverture du labyrinthe. 
    opening(200,200,400,180)                    # Création de la deuxième ouverture du labyrinthe.
    text(0,250)                                 # Création du bout de texte au dessus du labyrinthe.
  

# Appel de la fonction d'affichage :  
   
display()
mainloop()