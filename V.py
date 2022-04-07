# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:09:29 2022

@author: Thibault Grivel
"""

#trucs à faire et j'ai pas le temps: faire en sorte que la police soit intégré au programme, arriver à écrire des accents à partir du json, fixer cette boucle satanique
#l'itemconfig ne marche pas

from M import *

global type_bateau, position_valide


def definir_type_bateau():
    global bateau, bateau_actuel_image, type_bateau, position_valide, bateau_a_placer
    bateau_a_placer = bateau
    type_bateau = 0
    position_valide = False
    for i in range(len(bateau_a_placer)):
        if (type_bateau < bateau_a_placer[i]):
            type_bateau = i
    bateau_actuel = bat2big
    if (type_bateau == 3):
        bateau_actuel = bat3big
    elif(type_bateau == 4):
        bateau_actuel = bat4big
    elif(type_bateau == 5):
        bateau_actuel = bat5big
    if (type_bateau != 0):    
        bateau_actuel_image = cnv.create_image(positionX_origin, positionY_origin+5, anchor=NW, image=bateau_actuel)

#lance la partie
def lancer_partie():
    global tour, tc, grillex, grilley, grille, grille2, bateau, bateau2,nbat, nbat1, nbat2, bloquer_la_grille, grille3, grille4, positionX, positionY, type_bateau, horizontale, position_valide, tplacer, cplacer
    #images_feuille()
    #print(centre)
    #grille x et grille y à peut-être définir
    grille = [[0 for i in range(cote)] for j in range(cote)] #Joueur 1, 0: rien, 1:bateau, 2: bâteau touché, 3: tir raté, 4: bateau coulé
    grille2 = [[0 for i in range(cote)] for j in range(cote)] #Joueur 2 [[x0y0, x1y0, x3y0..],[x0y1, x1y1, x2y1..]
    grille3 = [[2 for i in range(cote)] for j in range(cote)] #grille de réflexion du joueur 1, 0: bateau coulé ou 100% rien, 1: bateau touché, 2: sais pas
    grille4 = [[2 for i in range(cote)] for j in range(cote)] #grille de réflexion du joueur 2
    #tour = 1; #1: joueur1, 2: joueur 2
    #bateaux
    bateau = [0, 0, 1, 2, 1, 1] #nombre de bateaux d'une certaine longueur, minimum de deux svp [0,1,2,3,4,etc]
    bateau2 = bateau
    nbat = 0
    for i in range(len(bateau)):
        nbat = nbat + bateau[i]
    #print(nbat)
    nbat1 = nbat #nombre de bateaux du joueur 1
    nbat2 = nbat #nombre de bateaux du joueur 2
    
    #placement aléatoire des bateaux sur la grille
    #grille_bateau(grille)
    grille_bateau(grille2)
    
    cnv.delete("all")
    afficher_feuille()
    afficher_grille()
    tplacer = cnv.create_text((largeur/7)*6, (hauteur/8)*1, text=dlangue['cagepla'], fill="#2439B5", font=("Distrait", 80, "bold"))
    position_valide = False
    definir_type_bateau()

def partie_commence():
    global tour
    cnv.delete(tplacer)
    
    for i in range(cote):
        for j in range(cote):
            if (grille[j][i]==2):
                grille[j][i]=0
    
    refresh()
    humain = cnv.create_image((largeur/7)*5, (hauteur/16)*2, anchor=NW, image=humain_content)
    machine = cnv.create_image((largeur/7)*5, (hauteur/16)*9, anchor=NW, image=machine_content)
    tindication1 = cnv.create_text((largeur/7)*6, (hauteur/16)*3, text="Raté", fill="#2439B5", font=("Distrait", 65, "bold"))
    tindication2 = cnv.create_text((largeur/7)*6, (hauteur/16)*10, text="Touché", fill="#2439B5", font=("Distrait", 65, "bold"))
    tjoueur1 = cnv.create_text((largeur/7)*6, (hauteur/16)*1, text=dlangue['jou_eur']+" 1:", fill="#2439B5", font=("Distrait", 80, "bold"))
    tbatres = cnv.create_text((largeur/7)*5, (hauteur/16)*5, text=dlangue['batres'], fill="#2439B5", anchor=NW, font=("Distrait", 50, "bold"))
    tbatcoul = cnv.create_text((largeur/7)*5, (hauteur/16)*6, text=dlangue['batcoul'], fill="#2439B5", anchor=NW, font=("Distrait", 50, "bold"))
    tjoueur2 = cnv.create_text((largeur/7)*6, (hauteur/16)*8, text=dlangue['jou_eur']+" 2:", fill="#2439B5", font=("Distrait", 80, "bold"))
    tbatres2 = cnv.create_text((largeur/7)*5, (hauteur/16)*12, text=dlangue['batres'], fill="#2439B5", anchor=NW, font=("Distrait", 50, "bold"))
    tbatcoul2 = cnv.create_text((largeur/7)*5, (hauteur/16)*13, text=dlangue['batcoul'], fill="#2439B5", anchor=NW, font=("Distrait", 50, "bold"))
    tour = 1

#place aléatoirement les bateaux
def grille_bateau(grille):
    rx = 0
    ry = 0
    directionx = 0
    directiony = 0
    grille3 = [[0 for i in range(cote+2)] for j in range(cote+2)]
    limiteur = 0
    
    for i in range(len(bateau)): #longueur des bateaux à placer
        for j in range(bateau[i]): #bateaux de longueur i à placer
            #print("i:",i)
            boule = False
            limiteur = 0
            while(boule==False and limiteur<1000): #se répète tant que le bateau ne s'est pas placé correctement
                rx = random.randrange(cote-i+1) #le x d'une case au pif pour placer un bout du bateau
                ry = random.randrange(cote-i+1) #le y d'une case au pif pour placer un bout du bateau
                directionx = random.randrange(2) #horizontal (directionx=1) ou vertical (directiony=1)
                directiony = 1-directionx
                boule=True
                for k in range(i):
                    #print(rx,ry,rx+(k-1)*directionx,ry+(k-1)*directiony,grille3[ry+(k-1)*directiony][rx+(k-1)*directionx])
                    if (grille[ry+k*directiony][rx+k*directionx]==2):
                        boule=False
                if (boule==False):
                    limiteur = limiteur+1
            if (ry+(-1)*directiony<cote and ry+(-1)*directiony>=0 and rx+(-1)*directionx<cote and rx+(-1)*directionx>=0):
                grille[ry+(-1)*directiony][rx+(-1)*directionx] = 2
            if (ry+(i)*directiony<cote and ry+(i)*directiony>=0 and rx+(i)*directionx<cote and rx+(i)*directionx>=0):
                grille[ry+(i)*directiony][rx+(i)*directionx] = 2
            for k in range(i):
                if (ry+k*directiony-1*directionx<cote and ry+k*directiony-1*directionx>=0 and rx+k*directionx-1*directiony<cote and rx+k*directionx-1*directiony>=0):
                    grille[ry+k*directiony-1*directionx][rx+k*directionx-1*directiony]=2
            for k in range(i):
                if (ry+k*directiony+1*directionx<cote and ry+k*directiony+1*directionx>=0 and rx+k*directionx+1*directiony<cote and rx+k*directionx+1*directiony>=0):
                    grille[ry+k*directiony+1*directionx][rx+k*directionx+1*directiony]=2
            grille[ry][rx] = 1 #premier bout du bateau
            for k in range(1,i-1,1): #milieux du bateau
                grille[ry+k*directiony][rx+k*directionx] = 1
            grille[ry+(i-1)*directiony][rx+(i-1)*directionx] = 1 #fin du bateau
    for i in range(cote):
        for j in range(cote):
            if (grille[j][i]==2):
                grille[j][i]=0

#dessine une feuille a4 pour le fond
def afficher_feuille():
    for i in range (((int)(hauteur/tc))+1): #de haut en bas
        for j in range (((int)(largeur/tc)), 0-1, -1): #de droite à gauche
            if (i==0):
                if (j>(int)((marge)/tc)):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car9)
                elif (j==(int)((marge)/tc)):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car8)
                else:
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car7)
            else:
                if (j>(int)((marge)/tc)):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car3)
                elif (j==(int)((marge)/tc)):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car2)
                else:
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car)

#♦dessine la grille
def afficher_grille():
    global select
    select = cnv.create_image(1920, 1080, anchor=NW, image=selectj)
    #Dessin de la grille
    for i in range (cote+2): #y
        for j in range (cote+2): #x
            placementx = grillex-tc+j*tc
            placementy = grilley+-tc+i*tc
            if (i==0 and j==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case2)
            elif (i==0 and j==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case4)
            elif (i==cote+1 and j==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case7)
            elif (i==cote+1 and j==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case9)
            elif (i==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case3)
                cnv.create_text(placementx+tc/2, placementy+tc/2+tc/8, text=j, fill="#2439B5", font=("Distrait", tc, "bold"))
            elif (j==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case5)
                if (cote<=26):
                    cnv.create_text(placementx+tc/2, placementy+tc/2+tc/8, text=chr(i+64), fill="#2439B5", font=("Distrait", tc, "bold"))
                    #print(tc, placementy)
                else:
                    cnv.create_text(placementx+tc/2-tc/3, placementy+tc/2+tc/8, text=chr((int)((i-1)/26+1+64))+chr((i-1)%26+1+64), fill="#2439B5", font=("Distrait", tc, "bold"))
            elif (j==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case6)
            elif (i==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case8)
            else:
                cnv.create_image(placementx, placementy, anchor=NW, image=case)

    for i in range (cote): #x
        for j in range (cote): #xy
             if (i<cote and j<cote):
                 placementx = ((int)((milieu*2-((int)(1920/tc)-marge))/2)-((int)(cote/2)))*tc+(i+1)*tc
                 cnv.create_text(placementx+50, (j+2)*tc+50, text=grille[i][j], fill="#2439B5", font=('Distrait 80 bold'))

#détecte si une touche est pressée
def touche_pressee(event):
    global mode_affichage, largeur, hauteur, tour
    kp = repr(event.char) #pour savoir quelle touche a été pressée
    #raccourci pour modifier la taille de l'écran
    if (kp == "'p'"):
        #print ("pressed x", repr(event.char))
        if (tour == 1):
            tour = 2
        else:
            tour = 1
        refresh()
    if (kp == "'q'"):
        partie_commence()

#détecte le mouvement de la souris
def origine(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      if (tour > 0):
          if (x>grillex and x<(grillex+cote*tc) and y>grilley and y<(grilley+cote*tc)):
              if (tour == 1 and grille2[(int)((x-grillex)/tc)][(int)((y-grilley)/tc)]!=2 and grille2[(int)((x-grillex)/tc)][(int)((y-grilley)/tc)]!=3):
                  cnv.coords(select, grillex+((int)((x-grillex)/tc))*tc, grilley+((int)((y-grilley)/tc))*tc)
              else:
                  cnv.coords(select, 1920, 1080)
          else:
              cnv.coords(select, 1920, 1080)

#détecte le clic de la souris
def origine_clic(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      if (tour == 1):
          if (x>grillex and x<(grillex+cote*tc) and y>grilley and y<(grilley+cote*tc)):
              placer_croix((int)((x-grillex)/tc),(int)((y-grilley)/tc))

#place un cercle, pour le placement manuel des bateaux
def placer_cercle(cx,cy,fin):
    global grille, horizontale, type_bateau, bateau_a_placer
    if (grille[cx][cy]==0):
       croicle2.append(cnv.create_image((cx+(grillex/tc))*tc, (cy+(grilley/tc))*tc, anchor=NW, image=cercle_bleu))
       grille[cx][cy] = 1
       if horizontale:
           print("plouf",fin,cx,cy)
           if (cx-1>=0):
               if (grille[cx-1][cy] == 0):
                   grille[cx-1][cy] = 2
           if (cy-1>=0):
               grille[cx][cy-1] = 2
           if (cy+1<cote):
               grille[cx][cy+1] = 2
           if (cx+1<cote and fin==0):
               grille[cx+1][cy] = 2
       else:
           print("plaf",fin,cx,cy)
           if (cy-1>=0):
               if (grille[cx][cy-1] == 0):
                   grille[cx][cy-1] = 2
           if (cx-1>=0):
               grille[cx-1][cy] = 2
           if (cx+1<cote):
               grille[cx+1][cy] = 2
           if (cy+1<cote and fin==0): #fin: si = 0, veut dire que c'est le dernier bout du bateau à placer 
               grille[cx][cy+1] = 2
       
       
#se lance quand le joueur clique sur une case, place une croix/carré
def placer_croix(cx,cy):
     global grille, grille2, tour, nbat1, nbat2, bateau, bateau2
     #print("j:",tour)
     if (tour > 0):
         if (grille2[cx][cy]>=1 and grille2[cx][cy]<2):
             croicle.append(cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=carre))
             #cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=lignev)
             grille2[cx][cy]=2
             #nbat2 = nbat2 - 1
             bateau2 = compteur_bato(grille2,bateau2)
             nbat2 = 0
             for i in range(len(bateau2)):
                 nbat2 = nbat2 + bateau2[i]
             print(tour,bateau,bateau2, nbat2)
             if (nbat2 == 0):
                 victoire()
             else:
                 joueur2()
         elif (grille2[cx][cy]==0):
             croicle.append(cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=croix_rouge))
             #print(grillex+cx*tc, grilley+cy*tc)
             grille2[cx][cy]=3
             joueur2()

#tour du joueur 2
def joueur2():
     global grille, grille2, tour, nbat1, nbat2, bateau, bateau2, grille3, grille4,rx,ry
     tour = 2
     #print (tour)
     #cnv.create_image(grillex+1*tc, grilley+1*tc, anchor=NW, image=selectr)
     #if (tour == 1):
     #    tour = 2
     #refresh()
     boule = False #pour savoir si l'image a pu être placée
     while (boule == False):
         #rx = random.randrange(cote)
         #ry = random.randrange(cote)
         ra = strat57(grille,grille4)
         rx = ra[0]
         ry = ra[1]
         if (grille[rx][ry]== 0 or grille[rx][ry]==1):
             boule = True
     
     #refresh()
     #cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=selectr)
     if (grille[rx][ry]==1):
         grille[rx][ry]=2
         refresh()
         croicle2.append(cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=cercle_rouge))
         cnv.itemconfig(croicle2[len(croicle2)-1], state='hidden')
         #☻cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=ligner)
         bateau = compteur_bato(grille,bateau)
         nbat1 = 0
         for i in range(len(bateau)):
             nbat1 = nbat1 + bateau[i]
         if (nbat1 == 0):
             defaite()
     elif (grille[rx][ry]==0):
        grille[rx][ry]=3
        #cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=selectr)
        croicle2.append(cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=croix_noir))
        cnv.itemconfig(croicle2[len(croicle2)-1], state='hidden')
     xamer = threading.Thread(target=timer)
     xamer.start()

#ia du joueur 2
def strat57(grille,griller): #griller: grille de réflexion
    print("début")
    #grille: grille de l'adversaire, griller: grille de réflexion
    #grille1-2, 0: rien, 1:bateau adverse, 2: bâteau adverse touché, 3: tir raté, 4: bateau coulé
    #grille3-4: bateau coulé ou 100% rien, 1: nouveau bateau touché, 2: sais pas 3: forte possibilité 4: bateau touché
    lde3 = [] #nombre de 3 dans la grille de réflexion
    #deux liste de 2 pour faire du une case sur 2
    lde2 = [] #nombre de 2 première partie damier dans la grille de réflexion
    lde2b = [] #nombre de 2 première partie damier dans la grille de réflexion
    for i in range(cote):
        for j in range(cote):
            #collecte des données de grille par griller
            if (grille[j][i]==3): #bateau posé, raté
                griller[j][i]=0 #case éliminée
            if (grille[j][i]==4): #bateau coulé
                griller[j][i]=0 #case éliminée
                if(j-1>=0):
                    griller[j-1][i]=0
                if(i-1>=0):
                    griller[j][i-1]=0
                if(j+1<cote):
                    griller[j+1][i]=0
                if(i+1<cote):
                    griller[j][i+1]=0
            if ((grille[j][i]==2 and griller[j][i]==2) or (grille[j][i]==2 and griller[j][i]==3)): #bateau touché
                griller[j][i]=1 #case avec un nouveau bateau touché dedans
                #check les 4 cases adjacentes pour voir s'il y a un autre bateau touché
                batad = 0 #1: il y a un bateau touché adjacent horizontalement,2:verticalement
                batadx = 0 #coordonnées du bateau adjacent
                batady = 0
                if(j-1>=0):
                    if(griller[j-1][i]==4):
                        batad = 1
                        batadx = j-1
                        batady = i
                if(i-1>=0):
                    if(griller[j][i-1]==4):
                        batad = 2
                        batadx = j
                        batady = i-1
                if(j+1<cote):
                    if(griller[j+1][i]==4):
                        batad = 1
                        batadx = j+1
                        batady = i
                if(i+1<cote):
                    if(griller[j][i+1]==4):
                       batad = 2
                       batadx = j
                       batady = i+1
                #recheck les 4 cases adjacentes, et les dénomine comme possiblement détentrices de bateaux adverses
                if(j-1>=0):
                    if(griller[j-1][i]==2):
                        if (batad == 2):
                            griller[j-1][i] = 0
                            griller[batadx-1][batady] = 0
                        else:
                            griller[j-1][i] = 3
                if(i-1>=0):
                    if(griller[j][i-1]==2):
                        if (batad == 1):
                            griller[j][i-1] = 0
                            griller[batadx][batady-1] = 0
                        else:
                            griller[j][i-1] = 3
                if(j+1<cote):
                    if(griller[j+1][i]==2):
                        if (batad == 2):
                            griller[j+1][i] = 0
                            griller[batadx+1][batady] = 0
                        else:
                            griller[j+1][i] = 3
                if(i+1<cote):
                    if(griller[j][i+1]==2):
                       if (batad == 1):
                           griller[j][i+1] = 0
                           griller[batadx][batady+1] = 0
                       else:
                           griller[j][i+1] = 3
                #check en dessous/au dessus, à gauche/à droite pour un autre bateau touché
                griller[j][i]=4 #deviens un vieux bateau coulé
    for i in range(cote):
        for j in range(cote):
            if (griller[j][i]==3):
                lde3.append([j,i])
            if (griller[j][i]==2):
                if ((i+j)%2==1):
                    lde2.append([j,i])
                else:
                    lde2b.append([j,i])
    if (len(lde3)>0):
        #print("l3")
        randoma = random.randrange(len(lde3))
        rx = lde3[randoma][0]
        ry = lde3[randoma][1]
    else:
        #print("l2")
        #print(len(lde2))
        randoma = random.randrange(len(lde2))
        rx = lde2[randoma][0]
        ry = lde2[randoma][1]
    for i in range (cote):
        for j in range (cote):
            print(grille[j][i],end=" ")
        print()
    print()
    for i in range (cote):
        for j in range (cote):
            print(griller[j][i],end=" ")
        print()
    print("fin",rx,ry, griller[rx][ry], grille[rx][ry])
    ra = [rx,ry]
    return ra

#comptele nombre de bateau après le tour du joueur 2
def compteur_bato(grille, bateau): #compte le nombre de bateau
    c = 0 #compteur de bouts de bateau
    d = 0 #compteur de bouts bateau touchés
    for i in range(len(bateau)):
        bateau[i]=0
    nbat=0
    for i in range(cote): #y
        for j in range(cote): #x
            #print("cb",c,j,i,1,0)
            if (grille[j][i]==0 or grille[j][i]==3):
                if (c>1 and c!=d):
                    bateau[c]=bateau[c]+1
                if (c>1 and c==d):
                    #print("g",grille[j-1][i])
                    bateau_mort(c,j-1,i,1,0)
                c=0
                d=0
            if (grille[j][i]==1 or grille[j][i]==2):
                c=c+1
            if (grille[j][i]==2):
                d=d+1
        if (c>1 and c!=d):
            bateau[c]=bateau[c]+1
        if (c>1 and c==d):
            bateau_mort(c,j,i,1,0)
        c=0
        d=0
    for j in range(cote): #x
        for i in range(cote): #y
            if (grille[j][i]==0 or grille[j][i]==3):
                if (c>1 and c!=d):
                    bateau[c]=bateau[c]+1
                if (c>1 and c==d):
                    bateau_mort(c,j,i-1,0,1)
                c=0
                d=0
            if (grille[j][i]==1 or grille[j][i]==2):
                c=c+1
            if (grille[j][i]==2):
                d=d+1
        if (c>1 and c!=d):
            bateau[c]=bateau[c]+1
        if (c>1 and c==d):
            bateau_mort(c,j,i,0,1)
        c=0
        d=0
    return bateau

#se lance quand un bateau meurt, et le raye
def bateau_mort(n,rx,ry,dirx,diry):
    global grille, grille2, tour, croicle2
    #print(tour, n,rx,ry,dirx,diry)
    #print("g1",grille[rx][ry])
    #print("g2",grille2[rx][ry])
    #for i in range (cote):
        #for j in range (cote):
                ##print((int)(grille2[j][i]), end=" ")
                #cnv.create_text(grillex+j*tc+tc*0.5, grilley+i*tc-tc*0q.5, text=grille2[j][i], fill="black", font=("Distrait", 20, "bold"))
        #print()
    #print()
    for k in range(n):
        placx = grillex+rx*tc-k*tc*dirx
        placy = grilley+ry*tc-k*tc*diry
        if (tour == 1):
            grille2[rx-dirx*k][ry-diry*k] = 4
            if (k==0): #joueur 1 a détruit un bateau du joueur 2
                if (dirx==1):
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev4))
                else:
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev6))
            elif (k==n-1):
                if (dirx==1):
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev2))
                else:
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev8))
            else:
                if (dirx==1):
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev3))
                else:
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev7))
            #cnv.itemconfig(croicle[len(croicle)-1], state='hidden')
        if (tour == 2): #joueur 2 a détruit un bateau du joueur 1
            grille[rx-dirx*k][ry-diry*k] = 4
            if (k==0):
                if (dirx==1):
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner4))
                else:
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner6))
            elif (k==n-1):
                if (dirx==1):
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner2))
                else:
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner8))
            else:
                if (dirx==1):
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner3))
                else:
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner7))
            cnv.itemconfig(croicle2[len(croicle2)-1], state='hidden')


#se lance après le tour 2, affiche les actions du joueur 2
def timer():
    global tour, posourisx2, posourisy2
    tour = 2
    sleep(0.5)
    refreshb()
    sleep(0.05)
    refreshn()
    if (rx-posourisx2<0):
        dirx = -1
    else:
        dirx = 1
    if (ry-posourisy2<0):
        diry = -1
    else:
        diry=1
    #print("dir:",rx-posourisx2,ry-posourisy2)
    #print(dirx,diry)
    gx=posourisx2
    gy=posourisy2
    sleep(0.2)
    rouge = cnv.create_image(grillex+posourisx2*tc, grilley+posourisy2*tc, anchor=NW, image=selectr)
    #print("objectif:",rx,ry,"départ:",posourisx2,posourisy2,"dir",dirx,diry)
    ioni = 0
    vitesse_souris = random.randrange(5)/10+0.1
    while(gx!=rx or gy!=ry):
        ioni=ioni+1
        boule = False
        if (gx==rx or gy==ry):
            if (gx==rx):
                #print("gy==ry")
                gy = gy+diry
            else:
                #print("gx==rx")
                gx = gx+dirx
        else:
            randoma = random.randrange(3)
            if (randoma==0):
                gx = gx+dirx
            if (randoma==1):
                gy = gy+diry
            if (randoma==2):
                gx = gx+dirx
                gy = gy+diry
            #print("gx=blabla et gy=blabla")
        vitesse_sourisb = random.randrange(5)/10+0.1
        if (vitesse_sourisb<vitesse_souris):
            vitesse_souris = vitesse_sourisb
        sleep(vitesse_souris)
        cnv.delete(rouge)
        #print("n",ioni, gx, gy)
        rouge = cnv.create_image(grillex+gx*tc, grilley+gy*tc, anchor=NW, image=selectr)
        
    
    posourisx2=rx
    posourisy2=ry
    for i in range(len(croicle2)):
        cnv.itemconfig(croicle2[len(croicle2)-1], state='normal')
    cnv.delete(rouge)
        
    sleep(0.1)
    #print(tour)
    tour = 1
    refreshb()
    sleep(0.1)
    refreshn()
    
#pour recharger la feuille
def refresh():
    for i in range(len(croicle)):
        if (tour == 1):
            cnv.itemconfig(croicle[i], state='normal')
        if (tour == 2):
            cnv.itemconfig(croicle[i], state='hidden')
    for i in range(len(croicle2)):
        if (tour == 1):
            cnv.itemconfig(croicle2[i], state='hidden')
        if (tour == 2):
            cnv.itemconfig(croicle2[i], state='normal')

def refreshb():
    for i in range(len(croicle)):
        if (tour == 2):
            cnv.itemconfig(croicle[i], state='hidden')
    for i in range(len(croicle2)):
        if (tour == 1):
            cnv.itemconfig(croicle2[i], state='hidden')

def refreshn():
    for i in range(len(croicle)):
        if (tour == 1):
            cnv.itemconfig(croicle[i], state='normal')
    for i in range(len(croicle2)-1):
        if (tour == 2):
            cnv.itemconfig(croicle2[i], state='normal')

def refreshn2():
    for i in range(len(croicle)):
        if (tour == 1):
            cnv.itemconfig(croicle[i], state='normal')
    for i in range(len(croicle2)):
        if (tour == 2):
            cnv.itemconfig(croicle2[i], state='normal')

#détecte le clic gauche enfoncé
def glisser_deposer_gauche(event):
    global bateau_attrape, positionX, positionY, type_bateau, horizontale, position_valide, bateau_actuel_image
    #if (tour == 2):
    #print(event.x, event.y)
    cnv.delete(bateau_actuel_image)
    
    if (type_bateau != 0):
        if (horizontale):
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+".png").resize((tc*type_bateau,tc)))
        else:
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+"b.png").resize((tc, tc*type_bateau)))
        position(event, bateau_attrape)

#"bouge" l'image
def position(event, image):
    global position_valide, bato, positionX, positionY, horizontale, type_bateau, bateau_attrape
    if (horizontale == True and (event.x <= grillex+tc*cote-(tc*(type_bateau-1)) and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote)) or (horizontale == False and (event.x <= grillex+tc*cote and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote-tc*(type_bateau-1))):
        positionX = event.x
        positionY = event.y
        if (horizontale == True and (event.x <= grillex+tc*cote-(tc*(type_bateau-1))  and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote)) or (horizontale == False and (event.x <= grillex+tc*cote and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote-tc*(type_bateau-1))):
            positionX = grillex+((int)((event.x-grillex)/tc))*tc
            positionY = grilley+((int)((event.y-grilley)/tc))*tc
        position_valide = True
    else:
        positionX = event.x
        positionY = event.y
        position_valide = False
    bato = cnv.create_image(positionX, positionY, image=image,anchor=NW)

#activé par le clic droit, tourne le bateau de 90 degrés
def rotation(event):
    global horizontale, positionX, positionY, bato, type_bateau, position_valide, bateau_attrape, bateau_actuel_image
    #if (tour == 2):
    cnv.delete(bateau_actuel_image)
    horizontale = not horizontale
        
    if (type_bateau != 0):
        if (horizontale):
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+".png").resize((tc*type_bateau,tc)))
        else:
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+"b.png").resize((tc, tc*type_bateau)))
        bato = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bateau_attrape, anchor=NW)

#activé quand le clic gauche est relâché
def valide(event):
    global tour, position_valide, positionX, positionY, type_bateau, horizontale, bato, grillex, grilley, bateau_actuel_image
    #if (tour == 2 and position_valide == True):
    
    if (position_valide==True and type_bateau!=0):
        for i in range(type_bateau):
            print(horizontale, int((positionX-grillex)/tc)+i,int((positionY-grilley)/tc), int((positionX-grillex)/tc)+i,int((positionY-grilley)/tc)-1, int((positionX-grillex)/tc)+i,int((positionY-grilley)/tc)+1,int((positionX-grillex)/tc)-1)
            if (horizontale and grille[int((positionX-grillex)/tc)+i][int((positionY-grilley)/tc)]!=0 and grille[int((positionX-grillex)/tc)+i][int((positionY-grilley)/tc)+1] != 0) or (not(horizontale) and grille[int((positionX-grillex)/tc)][int((positionY-grilley)/tc)+i]!=0):
                position_valide=False
                print("je suis ici")
        if position_valide :
            bateau_a_placer[type_bateau] -=1
            #boucle satanique, appelez un exorciste
            for i in range(type_bateau):
                if horizontale:
                    placer_cercle(int((positionX-grillex)/tc)+i, int((positionY-grilley)/tc),type_bateau-i) #débrouille toi pour qu'un truc à la place de type_bateau-i vale 0 à la fin de la boucle, que le bateau arrive à se placer, et ça marchera, je hais ta boucle
                else:
                    placer_cercle(int((positionX-grillex)/tc), int((positionY-grilley)/tc),type_bateau-i)
                cnv.delete(bato)
                cnv.delete(bateau_actuel_image)
                definir_type_bateau()
                print("qué?",i)
    elif (type_bateau == 0):
        partie_commence()
        print()

#se lancer quand le joueur 1 élimine tout les bateaux du joueur 2
def victoire():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="Bouillave l'ennemi, tu as!", fill="#FFC300", font=('Distrait 100 bold'))

#se lancer quand le joueur 2 élimine tout les bateaux du joueur 1
def defaite():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="petite crotte", fill="#00A513", font=('Distrait 200 bold'))