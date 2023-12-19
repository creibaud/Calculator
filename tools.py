from Stack import Stack

# Fonction pour séparer une chaine de caractère en une liste de caractères (similaire au .split() python
def separate(userInput, separator):
    listChar = []                       # Initialisation d'une liste vide
    groupOfChar = ""                    # Initialisation d'une chaine de caractère vide

    for char in userInput:              # Pour chaque caractère de la chaine de caractère
        if char == separator:           # Si le caractère est le séparateur
            listChar += [groupOfChar]   # On ajoute la chaine de caractère à la liste
            groupOfChar = ""            # On réinitialise la chaine de caractère
        else:
            groupOfChar += char         # Sinon on ajoute le caractère à la chaine de caractère pour former un mot, un nombre, ...

    listChar += [groupOfChar]           # On ajoute la dernière chaine de caractère à la liste
    return listChar

# Fonction pour savoir si un caractère est un nombre ou non (similaire au .isdigit() python)
def isNumber(char):
    try:
        float(char)       # On essaye de convertir le caractère en nombre car int("a") ou float("a") renvoie une erreur
        return True
    except:
        return False

# Fonction pour convertir un nombre en int ou float
def IntorFloat(number):
    if int(number) == float(number):        # Si le nombre est un entier (ex: 2.0 == 2)
        return int(number)
    return floatReduction(float(number))    # Sinon on réduit le nombre (ex: 2.0000000000000004 -> 2.0) ou (3.141592653589793 -> 3.141592653589793)

# Fonction pour calculer la valeur absolue d'un nombre (similaire au abs() python)
def absoluteValue(number):
    if number < 0:         # Si le nombre est négatif
        return -number     # On le multiplie par -1 pour le rendre positif
    return number

# Fonction pour arrondir un nombre flottant (similaire au round() python)
def roundFloat(number, decimal=None):
    stringNumber = str(number)              # On convertit le nombre en chaine de caractère pour pouvoir le séparer en deux parties
    listChar = separate(stringNumber, ".")  # On sépare le nombre en deux parties (partie entière et partie décimale)
    decimalPart = listChar[1]               # On récupère la partie décimale
    
    # Si on ne précise pas le nombre de décimales à garder
    if decimal is None:                 
        index = 0
        # On parcourt la partie décimale du nombre à partir de la fin pour trouver le premier chiffre différent (ex: 2.30000000000001 -> 3 est de la succession de 0)
        for i in range(len(decimalPart) - 2, 0, -1):
            index += 1
            if decimalPart[i] != decimalPart[i + 1]:
                break
        
        # On arrondie ce qui permet la réduction du nombre (ex: 2.30000000000001 -> 2.3)
        if int(decimalPart[index]) >= 5:
            decimalPart = decimalPart[:index - 2] + str(int(decimalPart[index] - 1) + 1)
        else:
            decimalPart = decimalPart[:index]
    elif decimal == 0:                              # On arrondie a l'entier le plus proche
        if int(decimalPart[0]) >= 5:
            listChar[0] = str(int(listChar[0]) + 1)
        decimalPart = ""
    else:                                           # On arrondie au nombre de décimales précisé
        if int(decimalPart[decimal]) >= 5:
            decimalPart = decimalPart[:decimal - 1] + str(int(decimalPart[decimal]) + 1)
        else:
            decimalPart = decimalPart[:decimal - 1]

    # Si la partie décimale est vide (ex: 2.0 -> 2)
    if decimalPart == "":
        return int(listChar[0])
    
    # On réecrie le nombre avec la partie décimale arrondie sous forme de string et on convertie le nombre en float
    return float(listChar[0] + "." + decimalPart)

# Fonction pour réduire un nombre flottant (ex: 2.0000000000000004 -> 2.0) ou (3.141592653589793 -> 3.141592653589793)
def floatReduction(number, precision=15):
    roundedNumber = roundFloat(number, precision)

    # Si la différence entre le nombre arrondi et le nombre initial est inférieur à 10^(-précision) on réduit le nombre
    if absoluteValue(roundedNumber - number) < 10 ** (-precision):
        return roundFloat(number)
    else:
        return number

# Fonction pour convertir une expression mathématique en notation (a, b, operator) ou (a, b, operator, c, operator) ...
def transcription(userInput):
    pile = Stack()                                  # Initialisation d'une pile vide
    listChar = separate(userInput, " ")             # Séparation de l'expression en une liste de caractères
    newExpression = ""                              # Initialisation d'une chaine de caractère vide

    for char in listChar:                           
        if isNumber(char):                          # Si le caractère est un nombre
            newExpression += char + " "             # On ajoute le nombre à la chaine de caractère
        
        if char == "(":                             # Si le caractère est une parenthèse ouvrante
            pile.push(char)                         # On empile la parenthèse
        
        if char == "*":                             # Si le caractère est un opérateur
            pile.push(char)                         # On empile l'opérateur
        
        if char == "+":                             # Si le caractère est un opérateur +
            while not pile.isEmpty():               # Tant que la pile n'est pas vide on dépile
                elt = pile.pop()

                if elt == "*":                      # Si l'élément dépiler est un opérateur *
                    newExpression += elt + " "      # On ajoute l'opérateur * à la chaine de caractère pour permettre la priorité des opérateurs * sur +
                else:                               # Sinon on réempile l'élément dépiler et on sort de la boucle
                    pile.push(elt)
                    break
            pile.push(char)                         # On empile l'opérateur + pour le mettre en temps que opérateur non prioritaire
        
        if char == ")":                             # Si le caractère est une parenthèse fermante
            while not pile.isEmpty():               # Tant que la pile n'est pas vide on dépile
                elt = pile.pop()

                if elt == "(":                      # Si l'élément dépiler est une parenthèse ouvrante on sort de la boucle
                    break
                else:
                    newExpression += elt + " "      # Sinon on ajoute l'élément dépiler à la chaine de caractère pour permettre la priorité des parenthèses
        
    while not pile.isEmpty():                       # Tant que la pile n'est pas vide on dépile
        elt = pile.pop()
        newExpression += elt + " "                  # On ajoute l'élément dépiler à la chaine de caractère
    
    return newExpression                            # On retourne la chaine de caractère pour permettre le calcul de l'expression (ex: 2 + 3 * 4 -> 2 3 4 * +)