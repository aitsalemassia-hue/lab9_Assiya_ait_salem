import numpy as np 
tableau_1d =np.array([1, 2, 3, 4, 5])
print("Tableau 1D :", tableau_1d)
tableau_2d = np.array([[1, 2, 3],[4, 5, 6]])
print("Tableau 2D :\n", tableau_2d)
zeros = np.zeros((2, 3))
print("Zeros :\n", zeros)
ones = np.ones((3, 2))
print("Ones :\n", ones)
progression = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8
print("np.arange :", progression)
progression = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8
print("np.arange :", progression)
print("dtype :", tableau_1d.dtype)  # type des éléments (int64, float64…)
print("ndim  :", tableau_1d.ndim)   # nombre de dimensions
print("shape :", tableau_1d.shape)  # tuple de dimensions
print("size  :", tableau_1d.size)   # nombre total d'éléments
print("dtype :", tableau_2d.dtype)  # type des éléments (int64, float64…)
print("ndim  :", tableau_2d.ndim)   # nombre de dimensions
print("shape :", tableau_2d.shape)  # tuple de dimensions
print("size  :", tableau_2d.size)   # nombre total d'éléments
#Restructurer un vecteur

#Créez un vecteur 1D :

vecteur = np.arange(1, 10)  # 1 à 9
print("Vecteur :", vecteur)

#Transformez-le en matrice 3×3 :

matrice = vecteur.reshape((3, 3))
print("Matrice 3x3 :\n", matrice)

#Vérifiez les tailles :

print("Shape :", matrice.shape)
print("Size  :", matrice.size)

#Dimension déduite automatiquement

matrice_auto = vecteur.reshape((3, -1))  # 3 lignes, colonnes calculées
print("Shape auto :", matrice_auto.shape)
