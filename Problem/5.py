class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Si la chaîne est vide → aucun palindrome
        if not s:
            return ""

        # On stocke le meilleur palindrome trouvé (début, fin)
        # On commence avec le premier caractère
        currPal = (0, 1)

        # On parcourt chaque caractère comme centre potentiel
        for i in range(len(s)):

            # Cas 1 : palindrome impair
            # Centre = un seul caractère (i, i)
            oddPal = self.expandAroundTheCenter(s, i, i)

            # Cas 2 : palindrome pair
            # Centre = entre deux caractères (i, i+1)
            evenPal = self.expandAroundTheCenter(s, i, i + 1)

            # On compare :
            # - le meilleur actuel
            # - le palindrome impair
            # - le palindrome pair
            # On garde le plus long
            currPal = max(currPal, oddPal, evenPal, key=lambda x: x[1] - x[0])

        # On retourne le palindrome trouvé dans la chaîne
        return s[currPal[0]: currPal[1]]

    def expandAroundTheCenter(self, s, left, right):

        # Tant que :
        # - on ne dépasse pas les bornes
        # - les caractères sont égaux
        while left >= 0 and right < len(s) and s[left] == s[right]:

            # On étend vers la gauche
            left -= 1

            # On étend vers la droite
            right += 1

        # À la sortie, on a dépassé le palindrome valide
        # Donc on retourne les indices corrigés
        return (left + 1, right)
