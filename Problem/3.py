"""
3. Longest Substring Without Repeating Characters :

Difficulté : Moyenne.

Approche :
On utilise la technique de la fenêtre glissante (Sliding Window).

On parcourt la chaîne caractère par caractère et on garde un ensemble
des caractères présents dans la fenêtre actuelle.

Si un caractère apparaît déjà dans la fenêtre, on déplace le début
de la fenêtre (`left`) jusqu'à ce que la sous-chaîne redevienne unique.

On calcule à chaque étape la longueur de la fenêtre et on garde la longueur
maximale trouvée.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):

        chars = set()          # Ensemble des caractères dans la fenêtre
        left = 0               # Début de la fenêtre
        max_length = 0         # Longueur maximale trouvée

        for right in range(len(s)):   # Parcourt chaque caractère

            while s[right] in chars:  # Tant que le caractère est déjà dans la fenêtre
                chars.remove(s[left]) # On retire le caractère le plus à gauche
                left += 1             # Et on déplace le début de la fenêtre

            chars.add(s[right])       # On ajoute le caractère actuel à la fenêtre

            max_length = max(max_length, right - left + 1)  # Met à jour la longueur maximale

        return max_length
