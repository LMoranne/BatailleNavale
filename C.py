# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:09:37 2022

@author: Thibault Grivel
"""

from V import *

lancer_partie()
root.bind("<KeyPress>", touche_pressee)
root.bind('<Motion>', origine) #détecte le mouvement de la souris
root.bind("<Button 1>",origine_clic) #détecte le clic gauche
root.bind("<Button 3>",rotation) #rotation
root.bind("<B1-Motion>", glisser_deposer_gauche) #détéction du mouvement de clic continue
root.bind("<ButtonRelease-1>", valide)  #détéction du dépot
cnv.pack()
root.mainloop()