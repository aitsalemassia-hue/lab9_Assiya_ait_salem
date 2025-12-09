import numpy as np
#1. Différence entre alist = [0]*6 et np.zeros(6)
alist=[0]*6
print("Liste alist :", alist) #la liste python ne permet pas les opérations vectorisées

np.zeros(6)
print("np.zeros(6) :", np.zeros(6)) # le tableau numpy permet des opérations directes sur l'ensemble des éléments

#2. Pourquoi np.linspace(0, 1, 5) inclut-il les bornes 0 et 1 
'''Parce que linspace génère un intervalle fermé [début, fin] divisé en N points uniformément espacés.'''
#3.
#reshape_vecteur = np.arange(9).reshape((4, 3))  #ValueError: cannot reshape array of size 9 into shape (4,3)
#print("np.reshape(4,3) :",reshape_vecteur ) # reshape permet de restructurer un tableau

#4.transformer un tableau en liste Python, et inversement pour du JSON 
tableau = np.array([1, 2, 3, 4, 5])
liste_python = tableau.tolist()  # Convertir en liste Python
print("Liste Python :", liste_python)
tableau_from_list = np.array(liste_python)  # Convertir en tableau NumPy
print("Tableau from list :", tableau_from_list)

import json

json_str = json.dumps(liste_python)  # Convertir en chaîne JSON
liste=json.loads(json_str)  # Convertir de chaîne JSON en liste Python
tableau_np = np.array(liste)  # Convertir en tableau NumPy
print("Tableau from JSON :", tableau_np)
