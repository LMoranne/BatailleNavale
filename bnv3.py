# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
from tkinter import *
from PIL import Image
from PIL import ImageTk
import threading
import random


root=Tk()

#taille de la fenêtre
l = 1920
h = 1080
cote = 7 #taille côté de la grille
tc = (int)(1080/(cote+3)) #taille des carreaux
centre = (int)(((int)(1920/tc))/2) #milieu de la largeur de la fenêtre (en cases)
marge = centre+(int)(cote/2)+1 #calcule la case de la marge
#print(centre)
grillex = ((int)((centre*2-((int)(1920/tc)-marge))/2)-((int)(cote/2)))*tc+tc; #x point en haut à gauche de la grille
grilley = 2*tc; #y
grille = [[0 for i in range(cote+1)] for j in range(cote+1)] #Joueur 1, 0: rien, 1:bateau, 2: bâteau détruit, 3: tir raté
grille2 = [[0 for i in range(cote+1)] for j in range(cote+1)] #Joueur 2 [[x0y0, x1y0, x3y0..],[x0y1, x1y1, x2y1..]
tour = 1; #1: joueur1, 2: joueur 2
#bateaux
bateau = [0, 5]
bateau2 = bateau
nbat = 0
for i in range(len(bateau)):
    nbat = nbat + bateau[i]
print(nbat)
nbat1 = nbat #nombre de bateaux du joueur 1
nbat2 = nbat #nombre de bateaux du joueur 2

"""for i in range(len(bateau)):
    for j in range(bateau[i]):
        boule = False
        while(boule==False):
            rx = random.randrange(cote)
            ry = random.randrange(cote)
            if (grille[rx][ry]==0):
                grille[rx][ry]=1
                boule=True
"""
for i in range(len(bateau2)):
    
    for j in range(bateau2[i]):
        rx = random.randrange(cote)
        ry = random.randrange(cote)
        grille2[rx][ry]=1

cnv = Canvas(root, width=l, height=h, bg='ivory')
#Création des images
#pour les carreaux
car = ImageTk.PhotoImage(Image.open("images/carreau.png").resize((tc, tc)))
car2 = ImageTk.PhotoImage(Image.open("images/carreau2.png").resize((tc, tc)))
car3 = ImageTk.PhotoImage(Image.open("images/carreau3.png").resize((tc, tc)))
car4 = ImageTk.PhotoImage(Image.open("images/carreau4.png").resize((tc, tc)))
car5 = ImageTk.PhotoImage(Image.open("images/carreau5.png").resize((tc, tc)))
car6 = ImageTk.PhotoImage(Image.open("images/carreau6.png").resize((tc, tc)))
car7 = ImageTk.PhotoImage(Image.open("images/carreau7.png").resize((tc, tc)))
car8 = ImageTk.PhotoImage(Image.open("images/carreau8.png").resize((tc, tc)))
car9 = ImageTk.PhotoImage(Image.open("images/carreau9.png").resize((tc, tc)))
#pour les cases
case = ImageTk.PhotoImage(Image.open("images/case.png").resize((tc, tc)))
case2 = ImageTk.PhotoImage(Image.open("images/case2.png").resize((tc, tc)))
case3 = ImageTk.PhotoImage(Image.open("images/case3.png").resize((tc, tc)))
case4 = ImageTk.PhotoImage(Image.open("images/case4.png").resize((tc, tc)))
case5 = ImageTk.PhotoImage(Image.open("images/case5.png").resize((tc, tc)))
case6 = ImageTk.PhotoImage(Image.open("images/case6.png").resize((tc, tc)))
case7 = ImageTk.PhotoImage(Image.open("images/case7.png").resize((tc, tc)))
case8 = ImageTk.PhotoImage(Image.open("images/case8.png").resize((tc, tc)))
case9 = ImageTk.PhotoImage(Image.open("images/case9.png").resize((tc, tc)))
#croix/cercle
croix_rouge = ImageTk.PhotoImage(Image.open("images/croix.png").resize((tc, tc)))
croix_noir = ImageTk.PhotoImage(Image.open("images/croixn.png").resize((tc, tc)))
cercle = ImageTk.PhotoImage(Image.open("images/cercle.png").resize((tc, tc)))
cercle_rouge = ImageTk.PhotoImage(Image.open("images/dercle.png").resize((tc, tc)))
carre = ImageTk.PhotoImage(Image.open("images/carre.png").resize((tc, tc)))
selectj = ImageTk.PhotoImage(Image.open("images/selectj.png").resize((tc, tc)))
selectr = ImageTk.PhotoImage(Image.open("images/selectr.png").resize((tc, tc)))
#ligne
ligner = ImageTk.PhotoImage(Image.open("images/ligner.png").resize((tc, tc)))
ligner2 = ImageTk.PhotoImage(Image.open("images/ligner2.png").resize((tc, tc)))
ligner3 = ImageTk.PhotoImage(Image.open("images/ligner3.png").resize((tc, tc)))
ligner4 = ImageTk.PhotoImage(Image.open("images/ligner4.png").resize((tc, tc)))
ligner5 = ImageTk.PhotoImage(Image.open("images/ligner5.png").resize((tc, tc)))
ligner6 = ImageTk.PhotoImage(Image.open("images/ligner6.png").resize((tc, tc)))
ligner7 = ImageTk.PhotoImage(Image.open("images/ligner7.png").resize((tc, tc)))
ligner8 = ImageTk.PhotoImage(Image.open("images/ligner8.png").resize((tc, tc)))
lignev = ImageTk.PhotoImage(Image.open("images/lignev.png").resize((tc, tc)))
lignev2 = ImageTk.PhotoImage(Image.open("images/lignev2.png").resize((tc, tc)))
lignev3 = ImageTk.PhotoImage(Image.open("images/lignev3.png").resize((tc, tc)))
lignev4 = ImageTk.PhotoImage(Image.open("images/lignev4.png").resize((tc, tc)))
lignev5 = ImageTk.PhotoImage(Image.open("images/lignev5.png").resize((tc, tc)))
lignev6 = ImageTk.PhotoImage(Image.open("images/lignev6.png").resize((tc, tc)))
lignev7 = ImageTk.PhotoImage(Image.open("images/lignev7.png").resize((tc, tc)))
lignev8 = ImageTk.PhotoImage(Image.open("images/lignev8.png").resize((tc, tc)))
#BAAAATTTTTTTTTEEEEEEAAAAAAAAAAAUUU
bat5 = ImageTk.PhotoImage(Image.open("images/bat5.png").resize((tc*5, tc)))
bat4 = ImageTk.PhotoImage(Image.open("images/bat4.png").resize((tc*4, tc)))
bat3 = ImageTk.PhotoImage(Image.open("images/bat3.png").resize((tc*3, tc)))
bat2 = ImageTk.PhotoImage(Image.open("images/bat2.png").resize((tc*2, tc)))
horizontale = True
position_valide = False
porte_avion = 1
croiseur = 1
contre_torpilleur = 2
torpilleur = 1
types_bateaux= [torpilleur, contre_torpilleur, croiseur, porte_avion]


#def chine_menu ():

def origine(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      if (x>grillex and x<(grillex+cote*tc) and y>grilley and y<(grilley+cote*tc)):
          if (tour == 1 and grille2[(int)((x-grillex)/tc)][(int)((y-grilley)/tc)]!=2 and grille2[(int)((x-grillex)/tc)][(int)((y-grilley)/tc)]!=3):
              cnv.coords(select, grillex+((int)((x-grillex)/tc))*tc, grilley+((int)((y-grilley)/tc))*tc)
          else:
              cnv.coords(select, 1920, 1080)
      else:
          cnv.coords(select, 1920, 1080)

def origine_clic(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      if (tour == 1):
          if (x>grillex and x<(grillex+cote*tc) and y>grilley and y<(grilley+cote*tc)):
              placer_croix((int)((x-grillex)/tc),(int)((y-grilley)/tc))

def presse(event):
    global tour, type_bateau
    kp = repr(event.char)
    #print ("pressed", kp) #repr(event.char))
    if (kp == "'p'" and tour == 2):
        #print ("pressed x", repr(event.char))
        cnv.delete("all")
        tour = 1
        chine_jeu()
        chine_grille()

def placer_cercle(cx,cy):
    global grille, horizontale, type_bateau
    if (grille[cx][cy]==0):
        #print(grille[cx][cy],cx,cy)
        #cnv.create_image(cx*tc, cy*tc, anchor=NW, image=cercle)
       grille[cx][cy] = 1
    
def placer_croix(cx,cy):
     global grille, grille2, tour, nbat1, nbat2
     if (grille2[cx][cy]==1):
         cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=carre)
         cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=lignev)
         grille2[cx][cy]=2
         nbat2 = nbat2 - 1
         if (nbat2 == 0):
             victoire()
     elif (grille2[cx][cy]==0):
         cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=croix_rouge)
         #print(grillex+cx*tc, grilley+cy*tc)
         grille2[cx][cy]=3
     cnv.create_image(grillex+1*tc, grilley+1*tc, anchor=NW, image=selectr)
     if (tour == 1):
         tour = 2
     tour = 2
     cnv.delete("all")
     chine_jeu ()
     chine_grille()
     boule = False #pour savoir si l'image a pu être placée
     while (boule == False):
         rx = random.randrange(cote)
         ry = random.randrange(cote)
         if (grille[rx][ry]== 0 or grille[rx][ry]==1):
             boule = True
     
     cnv.delete("all")
     chine_jeu ()
     chine_grille()
     cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=selectr)
     
     if (grille[rx][ry]==1):
         grille[rx][ry]=2
         cnv.delete("all")
         chine_jeu ()
         chine_grille()
         cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=cercle_rouge)
         cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=ligner)
         nbat1 = nbat1 - 1
         if (nbat1 == 0):
             defaite()
     elif (grille[rx][ry]==0):
        grille[rx][ry]=3
        cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=selectr)
        cnv.delete("all")
        chine_jeu ()
        chine_grille()
        cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=croix_noir)
             
def victoire():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="Bravo!", fill="#FFC300", font=('Distrait 100 bold'))
    
def defaite():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="C'est perdu", fill="#00A513", font=('Distrait 200 bold'))

def chine_jeu ():
    #Dessin de la feuille A4 en fond
    for i in range (((int)(1080/tc))+1):
        for j in range (((int)(1920/tc))+1):
            if (i==0):
                if (j>marge):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car6)
                elif (j==marge):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car5)
                else:
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car4)
            elif (i==1):
                if (j>marge):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car9)
                elif (j==marge):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car8)
                else:
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car7)
            else:
                if (j>marge):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car3)
                elif (j==marge):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car2)
                else:
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car)

def chine_grille ():
    global select, positionX, positionY, type_bateau, nbat2, horizontale, position_valide
    select = cnv.create_image(1920, 1080, anchor=NW, image=selectj)
    positionX_origin = 1150
    positionY_origin = 500
    position_valide = False
    #Dessin de la grille
    for i in range (cote+2): #y
        for j in range (cote+2): #x
            placementx = ((int)((centre*2-((int)(1920/tc)-marge))/2)-((int)(cote/2)))*tc+(j)*tc
            if (i==0 and j==0):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case2)
            elif (i==0 and j==cote+1):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case4)
            elif (i==cote+1 and j==0):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case7)
            elif (i==cote+1 and j==cote+1):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case9)
            elif (i==0):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case3)
                cnv.create_text(placementx+tc/2, (1+i)*tc+tc/2, text=j, fill="#2439B5", font=('Distrait 80 bold'))
            elif (j==0):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case5)
                if (cote<=26):
                    cnv.create_text(placementx+tc/2, (1+i)*tc+tc/2, text=chr(i+64), fill="#2439B5", font=('Distrait 80 bold'))
                else:
                    cnv.create_text(placementx+tc/2, (i+1)*tc+tc/2, text=chr((int)((i-1)/26+1+64))+chr((i-1)%26+1+64), fill="#2439B5", font=('Distrait 80 bold'))
            elif (j==cote+1):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case6)
            elif (i==cote+1):
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case8)
            else:
                cnv.create_image(placementx, (1+i)*tc, anchor=NW, image=case)
    for i in range (cote): #x
        for j in range (cote): #xy
             if (i<cote and j<cote):
                 placementx = ((int)((centre*2-((int)(1920/tc)-marge))/2)-((int)(cote/2)))*tc+(i+1)*tc
                 if (tour == 1):
                     if (grille2[i][j]==2):
                         cnv.create_image(placementx, (j+2)*tc, anchor=NW, image=carre)
                         cnv.create_image(placementx, (j+2)*tc, anchor=NW, image=lignev)
                     if (grille2[i][j]==3):
                         cnv.create_image(placementx, (j+2)*tc, anchor=NW, image=croix_rouge)
             if (tour == 2):
                 if (grille[i][j]==1):
                     cnv.create_image(placementx, (j+2)*tc, anchor=NW, image=cercle)
                 if (grille[i][j]==2):
                     cnv.create_image(placementx, (j+2)*tc, anchor=NW, image=cercle_rouge)
                     cnv.create_image(placementx, (j+2)*tc, anchor=NW, image=ligner)
                 if (grille[i][j]==3):
                     cnv.create_image(placementx, (j+2)*tc, anchor=NW, image=croix_noir)
    if (tour == 2):
        bateau_placer()
        if (nbat2 > 0):
            if (type_bateau == 2):
                bato2 = cnv.create_image(positionX_origin, positionY_origin, anchor=NW, image=bat2)
                
            elif (type_bateau == 3):
                bato3 = cnv.create_image(positionX_origin, positionY_origin, anchor=NW, image=bat3)
            
            elif (type_bateau == 4):
                bato4 = cnv.create_image(positionX_origin, positionY_origin, anchor=NW, image=bat4)
            
            elif (type_bateau == 5):
                bato3 = cnv.create_image(positionX_origin, positionY_origin, anchor=NW, image=bat5)
                
    #cnv.delete("all")
    
def glisser_deposer_gauche(event):
    global bat2, bat3, bat4, bat5, positionX, positionY, type_bateau, horizontale, position_valide
    if (tour == 2):
        #print(event.x, event.y)
        if (type_bateau == 2):
            if (horizontale):
                bat2 = ImageTk.PhotoImage(Image.open("images/bat2.png").resize((tc*2, tc)))
                position(event, bat2)
            else:
                bat2 = ImageTk.PhotoImage(Image.open("images/bat2b.png").resize((tc, tc*2)))
                position(event, bat2)
        elif (type_bateau == 3):
            if horizontale:
                bat3 = ImageTk.PhotoImage(Image.open("images/bat3.png").resize((tc*3, tc)))
                position(event, bat3)
            else:
                bat3 = ImageTk.PhotoImage(Image.open("images/bat3b.png").resize((tc, tc*3)))
                position(event, bat3)
        elif (type_bateau == 4):
            if horizontale:
                bat4 = ImageTk.PhotoImage(Image.open("images/bat4.png").resize((tc*4, tc)))
                position(event, bat4)
            else:
                bat4 = ImageTk.PhotoImage(Image.open("images/bat4b.png").resize((tc, tc*4)))
                position(event, bat4)
        elif (type_bateau == 5):
            if horizontale:
                bat5 = ImageTk.PhotoImage(Image.open("images/bat5.png").resize((tc*5, tc)))
                position(event, bat5)
            else:
                bat5 = ImageTk.PhotoImage(Image.open("images/bat5b.png").resize((tc, tc*5)))
                position(event, bat5)

def position(event, image):
    global position_valide, bato, positionX, positionY, horizontale, type_bateau
    if (horizontale == True and (event.x <= grillex+tc*cote-(tc*(type_bateau-1)) and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote-(tc*(type_bateau-1)))) or (horizontale == False and (event.x <= grillex+tc*cote and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote)):
        positionX = event.x
        positionY = event.y
        if (horizontale == True and (event.x <= grillex+tc*cote-(tc*(type_bateau-1))  and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote-(tc*(type_bateau-1)) )) or (horizontale == False and (event.x <= grillex+tc*cote and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote)):
            if horizontale:
                positionX = grillex+((int)((event.x-grillex)/tc))*tc
                positionY = grilley+((int)((event.y-grilley)/tc))*tc
            else:
                positionX = grillex+((int)((event.x-grillex)/tc))*tc
                positionY = grilley+((int)((event.y-grilley)/tc))*tc
        position_valide = True
    else:
        positionX = event.x
        positionY = event.y
        position_valide = False
    bato = cnv.create_image(positionX, positionY, image=image,anchor=NW)
        
def rotation(event):
    global horizontale, positionX, positionY, bat2, bat3, bat4, bat5, type_bateau, position_valide
    if (tour == 2):
        if (horizontale == True):
            horizontale = False
        else:
            horizontale = True
        if (type_bateau == 2):
            if horizontale:
                bat2 = ImageTk.PhotoImage(Image.open("images/bat2.png").resize((tc*2, tc)))
                bato2 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat2, anchor=NW)
            else:
                bat2 = ImageTk.PhotoImage(Image.open("images/bat2b.png").resize((tc, tc*2)))
                bato2 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat2, anchor=NW)
        elif (type_bateau == 3):
            if horizontale:
                bat3 = ImageTk.PhotoImage(Image.open("images/bat3.png").resize((tc*3, tc)))
                bato3 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat3, anchor=NW)
            else:
                bat3 = ImageTk.PhotoImage(Image.open("images/bat3b.png").resize((tc, tc*3)))
                bato3 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat3, anchor=NW)
        elif (type_bateau == 4):
            if horizontale:
                bat4 = ImageTk.PhotoImage(Image.open("images/bat4.png").resize((tc*4, tc)))
                bato4 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat4, anchor=NW)
            else:
                bat4 = ImageTk.PhotoImage(Image.open("images/bat4b.png").resize((tc, tc*4)))
                bato4 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat4, anchor=NW)
        elif (type_bateau == 5):
            if horizontale:
                bat5 = ImageTk.PhotoImage(Image.open("images/bat5.png").resize((tc*5, tc)))
                bato5 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat5, anchor=NW)
            else:
                bat5 = ImageTk.PhotoImage(Image.open("images/bat5b.png").resize((tc, tc*5)))
                bato5 = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bat5, anchor=NW)
            
def valide(event):
    global tour, position_valide, positionX, positionY, type_bateau, horizontale
    if (tour == 2 and position_valide == True):
        if (type_bateau == 2 and horizontale):
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-2, int(positionY/tc)-2)
        elif (type_bateau == 2 and horizontale != True):
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-1)
        elif(type_bateau == 3 and horizontale):
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-2, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-1, int(positionY/tc)-2)
        elif (type_bateau == 3 and horizontale != True):
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-1)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc))
        elif(type_bateau == 4 and horizontale):
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-2, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-1, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc), int(positionY/tc)-2)
        elif (type_bateau == 4 and horizontale != True):
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-1)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc))
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)+1)
        elif(type_bateau == 5 and horizontale):
            placer_cercle(int(positionX/tc), int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-4, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-2, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-1, int(positionY/tc)-2)
        elif (type_bateau == 5 and horizontale != True):
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-2)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)-1)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc))
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)+1)
            placer_cercle(int(positionX/tc)-3, int(positionY/tc)+2)
        types_bateaux[type_bateau-2] = types_bateaux[type_bateau-2] -1
        tour = 1
        chine_jeu()
        chine_grille()
        #récupérer la position des cercles
def bateau_placer():
    global type_bateau, torpilleur, contre_torpilleur, croiseur, porte_avion, types_bateaux
    types_bateaux_restants = []
    for i in range(len(types_bateaux)):
        if (types_bateaux[i] > 0):
            types_bateaux_restants.append(i+2)
    type_bateau = random.randint(min(types_bateaux_restants), max(types_bateaux_restants))
    print(type_bateau)
    #types_bateaux[type_bateau-2] = types_bateaux[type_bateau-2] -1
    #print(types_bateaux_restants)
chine_jeu()
chine_grille()
root.bind('<Motion>', origine) #détecte le mouvement de la souris
root.bind("<Button 1>",origine_clic) #détecte lppe clic gauche
root.bind("<KeyPress>", presse)
root.bind("<Button 3>",rotation)
root.bind("<B1-Motion>", glisser_deposer_gauche) #motion gauche
root.bind("<ButtonRelease-1>", valide)
cnv.pack()
root.mainloop()