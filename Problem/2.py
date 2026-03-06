
"""
2. Add Two Numbers :

Difficulté : Medium.

Approche :
On parcourt simultanément les deux listes chaînées représentant les nombres.
Chaque nœud contient un chiffre.

On additionne les chiffres correspondants ainsi que la retenue (carry).
On crée ensuite un nouveau nœud contenant le chiffre résultat.

On continue jusqu'à ce que les deux listes soient terminées.

La retenue est calculée avec divmod(val, 10).
"""

# Time: O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x          # Valeur stockée dans le noeud
        self.next = None      # Pointeur vers le noeud suivant


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)   # Noeud fictif pour simplifier la construction de la liste résultat
        current = dummy       # Pointeur pour construire la nouvelle liste
        carry = 0             # Variable pour stocker la retenue

        while l1 or l2:       # Continue tant qu'il reste des noeuds dans l'une des listes

            val = carry       # Initialise la somme avec la retenue précédente

            if l1:            # Si la première liste n'est pas vide
                val += l1.val # Ajouter la valeur du noeud
                l1 = l1.next  # Avancer dans la liste

            if l2:            # Si la deuxième liste n'est pas vide
                val += l2.val # Ajouter la valeur du noeud
                l2 = l2.next  # Avancer dans la liste

            carry, val = divmod(val, 10)  # Calculer la retenue et le chiffre à stocker

            current.next = ListNode(val)  # Créer un nouveau noeud avec le chiffre obtenu
            current = current.next        # Avancer le pointeur dans la liste résultat

        if carry == 1:        # Si une retenue reste à la fin
            current.next = ListNode(1) # Ajouter un dernier noeud

        return dummy.next     # Retourner la liste résultat (sans le noeud fictif)
