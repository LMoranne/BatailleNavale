# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:09:01 2022

@author: Thibault Grivel
"""

from tkinter import *
import tkinter as tk
from PIL import Image #pour les images
from PIL import ImageTk
import threading #pour le timer
import random
import json #pour la labgye
from threading import Thread #pour le timer
from time import sleep #pour le timer
global root, cote, horieontal
dlangue = json.load(open('langue/fr.json'))

root=Tk()

#affichage ordi ou téléphone
mode_affichage = 0 #0:ordi 1: téléphone

#Fenêtre
largeur = 1920 #largeur de la fenêtre
hauteur = 1080 #hauteur de la fenêtre
#if (largeur/hauteur<1.5):
#    largeur=hauteur*1.5
#if (largeur/hauteur>4):
#    hauteur=largeur*0.5
cnv = Canvas(root, width=largeur, height=hauteur, bg='ivory')
pdr = "cours" #pack de ressource

instant = "menu" #pour dire au programme à quel moment du jeu il en est c'est pour les bind en bas

croicle = [] #croix/carrés du joueur 1
croicle2 = [] #croix/carrés du joueur 2

#Paramètres de la grille et de la feuille
cote = 10 #taille côté de la grille, 10 c'est la taille réglementaire
tour = 0

#Création des images nécessaires pour le menu
sfeuille = ImageTk.PhotoImage(Image.open(pdr+"/feuille.png"))
sentoure = ImageTk.PhotoImage(Image.open(pdr+"/entoure.png"))
spas_entoure = ImageTk.PhotoImage(Image.open(pdr+"/pas_entoure.png"))

global grillex, grilley, taille_marge, marge, milieu, tc, car, car2, car3, car4, car5, car6, car7, car8, car9, case, case2, case3, case4, case5, case6, case7, case8, case9, croix_rouge, croix_noir, cercle, cercle_rouge, carre, selectj, selectr, ligner, ligner2, ligner3, ligner4, ligner5, ligner6, ligner7, ligner8, lignev, lignev2, lignev3, lignev4, lignev5, lignev6, lignev7, lignev8, bat5, bat4, bat3, bat2, horizontale, position_valide, porte_avion, croiseur, contre_torpilleur, torpilleur
if (mode_affichage == 0):
    tc = (int)(hauteur/(cote+3)) #taille des carreaux
    taille_marge = hauteur/2 #largeur de la marge
    marge = (int)((largeur-(taille_marge))/tc)*tc #coordonnée x ou y de la marge selon l'orientation de la grille
    if ((int)(marge/tc)%2==1 and cote%2==0):
        marge = marge -tc
    if ((int)(marge/tc)%2==0 and cote%2==1):
        marge = marge -tc
    milieu = marge/2 #milieu de la largeur de la feuille EN NE COMPTANT PAS LA MARGE
else:
    tc = (int)(largeur/(cote+3)) #taille des carreaux
    taille_marge = (hauteur/5)*2 #hauteur de la marge
    marge = (int)((hauteur-(taille_marge))/tc)*tc #coordonnée x ou y de la marge selon l'orientation de la grille
    milieu = largeur/2

grillex = milieu-((cote/2)*tc) #x du haut gauche de la grille
grilley = tc #y du haut gauche de la grille
#print(grillex, grilley)

#Création des images
#pour les carreaux
#change l'oriantation des images en fonction du mode d'affichage pour tourner la feuille
if (mode_affichage == 0):
    rotation = 0
else:
    rotation = 90
car = ImageTk.PhotoImage(Image.open(pdr+"/carreau.png").resize((tc, tc)).rotate(rotation))
car2 = ImageTk.PhotoImage(Image.open(pdr+"/carreau2.png").resize((tc, tc)).rotate(rotation))
car3 = ImageTk.PhotoImage(Image.open(pdr+"/carreau3.png").resize((tc, tc)).rotate(rotation))
car4 = ImageTk.PhotoImage(Image.open(pdr+"/carreau4.png").resize((tc, tc)).rotate(rotation))
car5 = ImageTk.PhotoImage(Image.open(pdr+"/carreau5.png").resize((tc, tc)).rotate(rotation))
car6 = ImageTk.PhotoImage(Image.open(pdr+"/carreau6.png").resize((tc, tc)).rotate(rotation))
car7 = ImageTk.PhotoImage(Image.open(pdr+"/carreau7.png").resize((tc, tc)).rotate(rotation))
car8 = ImageTk.PhotoImage(Image.open(pdr+"/carreau8.png").resize((tc, tc)).rotate(rotation))
car9 = ImageTk.PhotoImage(Image.open(pdr+"/carreau9.png").resize((tc, tc)).rotate(rotation))
#pour les cases
case = ImageTk.PhotoImage(Image.open(pdr+"/case.png").resize((tc, tc)))
case2 = ImageTk.PhotoImage(Image.open(pdr+"/case2.png").resize((tc, tc)))
case3 = ImageTk.PhotoImage(Image.open(pdr+"/case3.png").resize((tc, tc)))
case4 = ImageTk.PhotoImage(Image.open(pdr+"/case4.png").resize((tc, tc)))
case5 = ImageTk.PhotoImage(Image.open(pdr+"/case5.png").resize((tc, tc)))
case6 = ImageTk.PhotoImage(Image.open(pdr+"/case6.png").resize((tc, tc)))
case7 = ImageTk.PhotoImage(Image.open(pdr+"/case7.png").resize((tc, tc)))
case8 = ImageTk.PhotoImage(Image.open(pdr+"/case8.png").resize((tc, tc)))
case9 = ImageTk.PhotoImage(Image.open(pdr+"/case9.png").resize((tc, tc)))
#croix/cercle
croix_rouge = ImageTk.PhotoImage(Image.open(pdr+"/croix.png").resize((tc, tc)))
croix_noir = ImageTk.PhotoImage(Image.open(pdr+"/croixn.png").resize((tc, tc)))
cercle_bleu = ImageTk.PhotoImage(Image.open(pdr+"/cercle.png").resize((tc, tc)))
cercle_rouge = ImageTk.PhotoImage(Image.open(pdr+"/dercle.png").resize((tc, tc)))
carre = ImageTk.PhotoImage(Image.open(pdr+"/carre.png").resize((tc, tc)))
selectj = ImageTk.PhotoImage(Image.open(pdr+"/selectj.png").resize((tc, tc)))
selectr = ImageTk.PhotoImage(Image.open(pdr+"/selectr.png").resize((tc, tc)))
#ligne
ligner = ImageTk.PhotoImage(Image.open(pdr+"/ligner.png").resize((tc, tc)))
ligner2 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)))
ligner3 = ImageTk.PhotoImage(Image.open(pdr+"/ligner3.png").resize((tc, tc)))
ligner4 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)).rotate(180))
ligner5 = ImageTk.PhotoImage(Image.open(pdr+"/ligner.png").resize((tc, tc)).rotate(90))
ligner6 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)).rotate(90))
ligner7 = ImageTk.PhotoImage(Image.open(pdr+"/ligner3.png").resize((tc, tc)).rotate(90))
ligner8 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)).rotate(270))
lignev = ImageTk.PhotoImage(Image.open(pdr+"/lignev.png").resize((tc, tc)))
lignev2 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)))
lignev3 = ImageTk.PhotoImage(Image.open(pdr+"/lignev3.png").resize((tc, tc)))
lignev4 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)).rotate(180))
lignev5 = ImageTk.PhotoImage(Image.open(pdr+"/lignev.png").resize((tc, tc)).rotate(90))
lignev6 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)).rotate(90))
lignev7 = ImageTk.PhotoImage(Image.open(pdr+"/lignev3.png").resize((tc, tc)).rotate(90))
lignev8 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)).rotate(270))
#BAAAATTTTTTTTTEEEEEEAAAAAAAAAAAUUU
bat5 = ImageTk.PhotoImage(Image.open(pdr+"/bat5.png").resize((tc*5, tc)))
bat4 = ImageTk.PhotoImage(Image.open(pdr+"/bat4.png").resize((tc*4, tc)))
bat3 = ImageTk.PhotoImage(Image.open(pdr+"/bat3.png").resize((tc*3, tc)))
bat2 = ImageTk.PhotoImage(Image.open(pdr+"/bat2.png").resize((tc*2, tc)))
bat5b = ImageTk.PhotoImage(Image.open(pdr+"/bat5b.png").resize((tc, tc*5)))
bat4b = ImageTk.PhotoImage(Image.open(pdr+"/bat4b.png").resize((tc, tc*4)))
bat3b = ImageTk.PhotoImage(Image.open(pdr+"/bat3b.png").resize((tc, tc*3)))
bat2b = ImageTk.PhotoImage(Image.open(pdr+"/bat2b.png").resize((tc, tc*2)))
bat2big = ImageTk.PhotoImage(Image.open(pdr+"/bat2b.png").resize((tc*2, tc*4)))
bat3big = ImageTk.PhotoImage(Image.open(pdr+"/bat3b.png").resize((tc*2, tc*6)))
bat4big = ImageTk.PhotoImage(Image.open(pdr+"/bat4b.png").resize((tc*2, tc*7)))
bat5big = ImageTk.PhotoImage(Image.open(pdr+"/bat5b.png").resize((tc*2, tc*8)))
horizontale = False
position_valide = False

#d'accord
positionX_origin = 1500
positionY_origin = 250
positionX = 0
positionY = 0

#c vachement mieux
bato2 = []
bato3 = []
bato4 = []
bato5 = []
batos = [bato2, bato3, bato4, bato5]

"""def finPartie(VictoireOuDefaite):
    global tour
    tour=3
    if VictoireOuDefaite:
        texte="Bouillave l'ennemi, tu as!"
        remplissage="#FFC300"
    else:
        texte= "petite crotte"
        remplissage= "#00A513"
    cnv.create_text(960, 540, text=texte, fill=remplissage, font=('Distrait 100 bold'))"""


def victoire():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="Bouillave l'ennemi, tu as!", fill="#FFC300", font=('Distrait 100 bold'))
    
def defaite():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="petite crotte", fill="#00A513", font=('Distrait 200 bold'))
    