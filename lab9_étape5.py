import numpy as np
#Type et Formats
tableau_1=np.array([1,2,3,],dtype=np.float32)
print("Tableau 1D :", tableau_1)
tableau_1.astype(np.int32) # conversion en int32
print("dtype :", tableau_1.dtype)  # type des éléments (int32, float64…)
tableau_1.nbytes # taille en octets
print("nbytes :", tableau_1.nbytes)  # taille en octets
# Tableaux utilitaires
#Matrice identité
matrice_identite = np.eye(4)  # matrice identité 4x4
print("Matrice identité 4x4 :\n", matrice_identite)
#Tableau constant
Tableau_constant=np.full((2, 3), 7)  # matrice 2x3 remplie de 7
print("Tableau constant 2x3 rempli de 7 :\n", Tableau_constant)
#Restructurer un vecteur
reshape_vecteur = np.arange(12).reshape((4, 3))  # vecteur 1D de 0 à 11 en matrice 4x3
print("Reshape vecteur 1D en matrice 4x3 :\n", reshape_vecteur)
# Opérations vectorisées
# Exemple de matrice
matrice = np.array([[1, 2], [3, 4]])

# Multiplication de chaque élément
print("Matrice * 10 :\n", matrice * 10)

# Racine carrée sur un vecteur
vecteur = np.array([1, 4, 9, 16])
print("\nRacine carrée :\n", np.sqrt(vecteur))
# Somme des éléments d'une matrice
somme_totale = np.sum(matrice)     # somme de tous les éléments
print("la somme total est :",somme_totale)
