"""
4. Median of Two Sorted Arrays :

Difficulté : Difficile.
Time complexity : O(m+n)
Space complexity : O(m+n)

Approche :
On utilise une technique similaire à l'étape de fusion de l'algorithme
de tri fusion (Merge Sort).

Les deux tableaux sont déjà triés. On les parcourt donc simultanément
avec deux pointeurs.

À chaque étape, on ajoute le plus petit élément des deux tableaux dans
une nouvelle liste fusionnée.

Une fois la fusion terminée, on calcule la médiane :
- Si la taille de la liste est impaire, on retourne l'élément du milieu.
- Si la taille est paire, on retourne la moyenne des deux éléments du milieu.
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        liste = []   # Liste qui va contenir les deux tableaux fusionnés
        i = 0        # Pointeur pour nums1
        j = 0        # Pointeur pour nums2

        # Parcourt les deux listes tant qu'il reste des éléments dans les deux
        while i < len(nums1) and j < len(nums2):

            # Compare les éléments actuels
            if nums1[i] <= nums2[j]:
                liste.append(nums1[i])  # Ajoute le plus petit
                i += 1                  # Avance dans nums1
            else:
                liste.append(nums2[j])  # Ajoute le plus petit
                j += 1                  # Avance dans nums2

        # Ajoute les éléments restants de nums1 s'il en reste
        while i < len(nums1):
            liste.append(nums1[i])
            i += 1

        # Ajoute les éléments restants de nums2 s'il en reste
        while j < len(nums2):
            liste.append(nums2[j])
            j += 1

        # Trouve l'indice du milieu
        milieu = len(liste) // 2

        # Si la taille est impaire
        if len(liste) % 2 != 0:
            return liste[milieu]

        # Si la taille est paire → moyenne des deux valeurs centrales
        return float((liste[milieu] + liste[milieu - 1]) / 2)
