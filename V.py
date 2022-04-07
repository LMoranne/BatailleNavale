# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:09:29 2022

@author: Thibault Grivel
"""

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

def lancer_partie():
    global tour, tc, grillex, grilley, grille, grille2, bateau, bateau2,nbat, nbat1, nbat2, bloquer_la_grille, grille3, grille4, positionX, positionY, type_bateau, horizontale, position_valide
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
    #boucle pour afficher les grilles sur la console
    for i in range (cote):
        for j in range (cote):
            if (grille[j][i]!=0):
                if (grille[j][i]==1):
                    print((int)(grille[j][i]), end=" ")
                else:
                    print((int)(grille[j][i]*10-10), end=" ")
                #cnv.create_text(grillex+j*tc+tc*0.5, grillex+i*tc-tc*1.5, text=grille2[j][i], fill="black", font=("Distrait", 20, "bold"))
            else:
                print(grille[j][i], end=" ")
        print()
    print()
    for i in range (cote):
        for j in range (cote):
            if (grille2[j][i]!=0):
                if (grille2[j][i]==1):
                    print((int)(grille2[j][i]), end=" ")
                else:
                    print((int)(grille2[j][i]*10-10), end=" ")
                #cnv.create_text(grillex+j*tc+tc*0.5, grilley+i*tc-tc*0q.5, text=grille2[j][i], fill="black", font=("Distrait", 20, "bold"))
            else:
                print(grille2[j][i], end=" ")
        print()
    print()
    
    #print(grille2[2][4])
    placer_bateau()
    
    position_valide = False
    definir_type_bateau()
            
def placer_bateau():
    global tplacer, cplacer
    #print("pa")
    tplacer = cnv.create_text((largeur/7)*6, (hauteur/8)*1, text=dlangue['cagepla'], fill="#2439B5", font=("Distrait", 80, "bold"))
    
def partie_commence():
    global tour
    cnv.delete(tplacer)
    
    tjoueur1 = cnv.create_text((largeur/7)*6, (hauteur/8)*1, text=dlangue['jou_eur']+" 1:", fill="#2439B5", font=("Distrait", 80, "bold"))
    tbatres = cnv.create_text((largeur/7)*6, (hauteur/8)*2, text=dlangue['batres'], fill="#2439B5", font=("Distrait", 50, "bold"))
    tbatcoul = cnv.create_text((largeur/7)*6, (hauteur/8)*3, text=dlangue['batcoul'], fill="#2439B5", font=("Distrait", 50, "bold"))
    tjoueur2 = cnv.create_text((largeur/7)*6, (hauteur/8)*4, text=dlangue['jou_eur']+" 2:", fill="#2439B5", font=("Distrait", 80, "bold"))
    tbatres2 = cnv.create_text((largeur/7)*6, (hauteur/8)*5, text=dlangue['batres'], fill="#2439B5", font=("Distrait", 50, "bold"))
    tbatcoul2 = cnv.create_text((largeur/7)*6, (hauteur/8)*6, text=dlangue['batcoul'], fill="#2439B5", font=("Distrait", 50, "bold"))
    tour = 1
    
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
                #print(rx,ry,rx+k*directionx-1*directiony,ry+k*directiony-1*directionx,grille3[ry+k*directiony-1*directionx][rx+k*directionx-1*directiony])
                if (ry+k*directiony-1*directionx<cote and ry+k*directiony-1*directionx>=0 and rx+k*directionx-1*directiony<cote and rx+k*directionx-1*directiony>=0):
                    grille[ry+k*directiony-1*directionx][rx+k*directionx-1*directiony]=2
            for k in range(i):
                #print(rx,ry,rx+k*directionx+1*directiony,ry+k*directiony+1*directionx,grille3[ry+k*directiony+1*directionx][rx+k*directionx+1*directiony])
                if (ry+k*directiony+1*directionx<cote and ry+k*directiony+1*directionx>=0 and rx+k*directionx+1*directiony<cote and rx+k*directionx+1*directiony>=0):
                    grille[ry+k*directiony+1*directionx][rx+k*directionx+1*directiony]=2
            grille[ry][rx] = 1 #premier bout du bateau
            #grille3[ry+1][rx+1] = 1 #premier bout du bateau
            #print("bout:",directionx,directiony, i,rx,ry)
            for k in range(1,i-1,1): #milieux du bateau
                grille[ry+k*directiony][rx+k*directionx] = 1
                #grille3[ry+k*directiony+1][rx+k*directionx+1] = 1
                #grille[ry+k*directiony][rx+k*directionx] = k+1
                #print(rx+k*directionx,ry+k*directiony)
            grille[ry+(i-1)*directiony][rx+(i-1)*directionx] = 1 #fin du bateau
            #grille3[ry+(i-1)*directiony+1][rx+(i-1)*directionx+1] = 1
            #grille[ry+(i-1)*directiony][rx+(i-1)*directionx] = 9 #fin du bateau
            #print("fin:", rx+(i-1)*directionx, ry+(i-1)*directiony)
    #print(grille)
    #print(grille)
    #print(grille3)
    for i in range(cote):
        for j in range(cote):
            if (grille[j][i]==2):
                grille[j][i]=0

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
    if (kp == "'a'"):
        if (mode_affichage==0):
            root.geometry('608x1080')
            largeur = 608
            hauteur = 1080
            mode_affichage = 1
        else:
            root.geometry('1920x1080')
            largeur = 1920
            hauteur = 1080
            mode_affichage = 0
        #b = largeur
        #largeur = hauteur pour téléphone, ça dépasse de l'écran au sinon
        #hauteur = largeur
        images_feuille()
        cnv.config(width=largeur, height=hauteur) #redimensionne le canvas
        refresh()
    if (kp == "'q'"):
        partie_commence()
        
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

def origine_clic(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      if (tour == 1):
          if (x>grillex and x<(grillex+cote*tc) and y>grilley and y<(grilley+cote*tc)):
              placer_croix((int)((x-grillex)/tc),(int)((y-grilley)/tc))
              
def placer_cercle(cx,cy):
    global grille, horizontale, type_bateau, bateau_a_placer
    if (grille[cx][cy]==0):
       cnv.create_image((cx+(grillex/tc))*tc, (cy+(grilley/tc))*tc, anchor=NW, image=cercle_bleu)
       grille[cx][cy] = 1
       

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
                 xamer = threading.Thread(target=timer)
                 xamer.start()
         elif (grille2[cx][cy]==0):
             croicle.append(cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=croix_rouge))
             #print(grillex+cx*tc, grilley+cy*tc)
             grille2[cx][cy]=3
             joueur2()
             xamer = threading.Thread(target=timer)
             xamer.start()

def joueur2():
     global grille, grille2, tour, nbat1, nbat2, bateau, bateau2, grille3, grille4
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

def strat57(grille,griller): #griller: grille de réflexion
    rx = random.randrange(cote)
    ry = random.randrange(cote)
    #for i in range(cote):
    #    for j in range(cote):
    #        if (grille[j][i]==1 and griller[j][i]==2):
    #            
    ra = [rx,ry]
    return ra

def compteur_bato(grille, bateau): #compte le nombre de bateau
    c = 0 #compteur de bouts de bateau
    d = 0 #compteur de bouts bateau touchés
    for i in range(len(bateau)):
        bateau[i]=0
    nbat=0
    for i in range(cote): #y
        for j in range(cote): #x
            print("cb",c,j,i,1,0)
            if (grille[j][i]==0 or grille[j][i]==3):
                if (c>1 and c!=d):
                    bateau[c]=bateau[c]+1
                if (c>1 and c==d):
                    print("g",grille[j-1][i])
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

def bateau_mort(n,rx,ry,dirx,diry):
    global grille, grille2, tour
    print(tour, n,rx,ry,dirx,diry)
    print("g1",grille[rx][ry])
    print("g2",grille2[rx][ry])
    for i in range (cote):
        for j in range (cote):
                print((int)(grille2[j][i]), end=" ")
                #cnv.create_text(grillex+j*tc+tc*0.5, grilley+i*tc-tc*0q.5, text=grille2[j][i], fill="black", font=("Distrait", 20, "bold"))
        print()
    print()
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

def timer():
    global tour
    tour = 2
    sleep(0.5)
    refreshb()
    sleep(0.05)
    refreshn()
    sleep(1)
    cnv.itemconfig(croicle2[len(croicle2)-1], state='normal')
    sleep(1)
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

def glisser_deposer_gauche(event):
    global bateau_attrape, positionX, positionY, type_bateau, horizontale, position_valide, bateau_actuel_image
    #if (tour == 2):
    #print(event.x, event.y)
    cnv.delete(bateau_actuel_image)
    if (horizontale):
        bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+".png").resize((tc*type_bateau,tc)))
    else:
        bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+"b.png").resize((tc, tc*type_bateau)))
    
    if (type_bateau != 0):
        position(event, bateau_attrape)

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
        
def rotation(event):
    global horizontale, positionX, positionY, bato, type_bateau, position_valide, bateau_attrape, bateau_actuel_image
    #if (tour == 2):
    cnv.delete(bateau_actuel_image)
    horizontale = not horizontale
        
    if (horizontale):
        bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+".png").resize((tc*type_bateau,tc)))
    else:
        bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+"b.png").resize((tc, tc*type_bateau)))
    if (type_bateau != 0):
        bato = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bateau_attrape, anchor=NW)

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
            for i in range(type_bateau):
                if horizontale:
                    placer_cercle(int((positionX-grillex)/tc)+i, int((positionY-grilley)/tc))
                else:
                    placer_cercle(int((positionX-grillex)/tc), int((positionY-grilley)/tc)+i)
                cnv.delete(bato)
                cnv.delete(bateau_actuel_image)
                definir_type_bateau()
    elif (type_bateau == 0):
        joueur2()
        print()
    #chine_jeu()
    #chine_grille()



"""def finPartie(VictoireOuDefaite):
    global tour
    tour=3
    if VictoireOuDefaite:
        texte="Bouillave l'ennemi, tu as!"
        remplissage="#FFC300"
    else:
        texte=
        remplissage=
    cnv.create_text(960, 540, text=texte, fill=remplissage, font=('Distrait 100 bold'))"""


def victoire():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="Bouillave l'ennemi, tu as!", fill="#FFC300", font=('Distrait 100 bold'))
    
def defaite():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="petite crotte", fill="#00A513", font=('Distrait 200 bold'))