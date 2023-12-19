# Classe orientée objet pour la pile
class Stack:
    def __init__(self):
        # Initialisation d'une pile vide
        self.pile = []

    # Fonction pour empiler un élément à la pile (similaire au .append() python)
    def push(self, elt):
        self.pile += [elt]

    # Fonction pour depiler le dernier élément de la pile (similaire au .pop() python)
    def pop(self):
        top = self.pile[-1]             # On récupère le dernier élément de la pile
        self.pile = self.pile[:-1]      # On supprime le dernier élément de la pile
        return top
    
    # Fonction pour verifier si la pile est vide
    def isEmpty(self):
        if self.size() == 0:
            return True
        return False
    
    # Fonction pour connaitre la taille de la pile (similaire au len() python)
    def size(self):
        count = 0
        for elt in self.pile:
            count += 1
        return count