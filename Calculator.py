from Stack import Stack
from tools import separate, isNumber, IntorFloat

# Fonction pour effectuer une opération entre deux nombres (a et b) avec un opérateur (+ ou *)
def operation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "*":
        return a * b

# Fonction pour calculer une expression mathématique avec sous la forme (a, b, operator) ou (a, b, operator, c, operator) ...
def calculator(userInput):
    pile = Stack()                      # Initialisation d'une pile vide
    listChar = separate(userInput, " ") # Séparation de l'expression en une liste de caractères
    
    for char in listChar:
        # Si le caractère est un opérateur
        if char in ["+", "*"]:
            # On récupère les deux derniers nombres de la pile
            a = pile.pop()
            b = pile.pop()

            result = operation(a, b, char)  # On effectue l'opération entre les deux nombres
            pile.push(result)               # On empile le résultat de l'opération
        elif isNumber(char):                # Si le caractère est un nombre 
            pile.push(float(char))          # On empile le nombre

    return IntorFloat(pile.pop())      # On retourne le dernier nombre de la pile (le résultat de l'expression) en format int ou float
