"""
from Calculator import calculator
from tools import transcription

# Couleur jaune pour le texte affiché dans le terminal
YELLOW = "\033[33m"
BLUE = "\033[94m"
RESET = "\033[0m"      # Couleur par défaut pour le texte affiché dans le terminal

print(YELLOW + "<" + "=" * 84 + ">" + RESET)
print(YELLOW + "|" + RESET + " Pour utiliser le programme vous devez entrer une expression mathématique classique " + YELLOW + "|" + RESET)
print(YELLOW + "|" + RESET + " mais entre chaque caractère vous devez mettre un ESPACE.                           " + YELLOW + "|" + RESET)
print(YELLOW + "|" + RESET + " Exemple : 2 + 3 * 4                                                                " + YELLOW + "|" + RESET)
print(YELLOW + "|" + RESET + " Exemple : 2 + ( 3 + 4 + 6 ) * 5                                                    " + YELLOW + "|" + RESET)
print(YELLOW + "|" + RESET + " Pour les nombre negatif il faut coller l'operateur au nombre                       " + YELLOW + "|" + RESET)
print(YELLOW + "|" + RESET + " Exemple : 2 + -3 * 4                                                               " + YELLOW + "|" + RESET)   
print(YELLOW + "|" + RESET + " Exemple : 2 + ( 3 + 4 + -6 ) * 5                                                   " + YELLOW + "|" + RESET) 
print(YELLOW + "|" + RESET + " Exemple : -3 - 4 - 2 i faut faire -3 + -4 + -2                                     " + YELLOW + "|" + RESET)
print(YELLOW + "<" + "=" * 84 + ">" + RESET)
print()

userInput = input(f"Entrer une expression mathématique : \033[94m")     # Exemple : 2 + 3 * 4
tradInput = transcription(userInput)                                    # Exemple : 2 3 4 * +
result = calculator(tradInput)                                          # Exemple : 14
print(f"{RESET}On a : {userInput} = {result}")                          # Exemple : 2 + 3 * 4 = 14
"""

from UI import UI

ui = UI()
ui.run()