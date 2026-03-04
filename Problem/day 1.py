"""
1. Two sum : 
Difficulté : Facile.
Approche : Utilisation d'un dictionnaire pour le stockage les nombres et leurs indices
qui est le dictionnaire ici: et également cherchant le complément de chaque nombre dans 
la liste de sorte à atteindre le target voulu.

"""

class Solution:
  def twoSum(self, nums: List[int], target : int) -> List[int]:

    dictionnaire  = {} #Dictionnaire vide pour stocker un nombre etson  indice.
    for i, num in enumerate(nums): # Parcourt tous les nombres avec leur indice
      complément = target - num # Calcul du complément nécessaire pour atteindre la cible
      if complément in dictionnaire: # Vérifie si le complément existe déjà dans le dictionnaire
        return [dictionnaire[compl], i] # Si oui, on retourne les indices des deux nombres
      dictionnaire[num] = i # Sinon, ajoute le nombre actuel au dictionnaire pour futur usage
