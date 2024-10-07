#### Imports et définition des variables globales
"""Importation du module pour plus de récursivité"""
import sys
sys.setrecursionlimit(1200)
#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    caracteres=[]
    occurences=[]
    if not s:  # Si la chaîne est vide, on retourne une liste vide
        return []

    caracteres.append(s[0]) # On ajoute le premier caractère à la liste C
    occurences.append(1)

    for k in range(1,len(s)):
        if s[k] == s[k-1]:
            occurences[-1] += 1
        else:
            caracteres.append(s[k])
            occurences.append(1)

    return [(caracteres[i], occurences[i]) for i in range(len(caracteres))]

def artcode_r(s, compteur=1):
    """retourne la liste de tuples selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:  # Cas de base : si la chaîne est vide, on retourne une liste vide
        return []
    # Si le caractère actuel est identique au suivant, on incrémente le compteur
    for i in range(1, len(s)):
        if s[i] == s[0]:
            compteur += 1
        else:
            break
    # retourne le caractère actuel avec son compteur et réinitialise le compteur à 1
    return [(s[0], compteur)] + artcode_r(s[compteur:])
 #### Fonction principale
def main():
    """ Test les fonctions principales"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
