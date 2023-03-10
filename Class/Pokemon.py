import json
import random

class Pokemon: # ici on définit la classe Pokemon qui est la classe mère de toutes les autres classes
    def __init__(self,nom,niveau,type_pokemon,pv=100,attaque=0,defense=0): # on définit les attributs de la classe Pokemon
        self.__nom = nom  # on définit les attributs de la classe Pokemon
        self.niveau = niveau
        self.type_pokemon = type_pokemon
        self.__pv = pv
        self.attaque = attaque
        self.defense = defense

    def __str__(self): # on définit la méthode __str__ qui permet d'afficher les attributs de la classe Pokemon
        return f"{self.__nom} est de niveau {self.niveau} et est de type {self.type_pokemon}." # on retourne les attributs de la classe Pokemon

    def attaquer(self,adversaire): # on définit la méthode attaquer qui permet à un pokemon d'attaquer un autre pokemon
        precision = random.randint(0,100)  # on définit la précision de l'attaque
        if precision <= 90: # si la précision est inférieure ou égale à 90
            degats = self.attaque - adversaire.defense  # on définit les dégâts de l'attaque
            if degats < 0: # si les dégâts sont inférieurs à 0
                degats = 0 # on définit les dégâts à 0
            adversaire.__pv -= degats  # on définit les points de vie de l'adversaire
            print(f"{self.__nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.") # on affiche le nom du pokemon qui attaque, le nom de l'adversaire et les dégâts infligés
            if adversaire.pv <= 0:
                print(f"{adversaire.nom} est K.O.")
                return self.__nom
        else:
            print(f"{self.__nom} attaque {adversaire.nom} et rate son attaque.")

    def get_nom(self): # on définit la méthode get_nom qui permet de récupérer le nom du pokemon
        return self.__nom
    def get_pv(self):
        return self.__pv

    def set_pv(self, pv):
        self.__pv = pv

    def set_nom(self, nom):
        self.__nom = nom
class PokemonNormal(Pokemon): # ici on définit la classe PokemonNormal qui est une classe fille de la classe Pokemon
    def __init__(self,nom,niveau):
        super().__init__(nom,niveau,"normal",pv=100,attaque=10,defense=10)


class PokemonEau(Pokemon): # ici on définit la classe PokemonEau qui est une classe fille de la classe Pokemon
    def __init__(self, nom, attaque):
        super().__init__(nom, 100, attaque, 0, "Eau")
        self._Pokemon__pv = 100

    def get_pv(self):
        return self._Pokemon__pv


class PokemonFeu(Pokemon): # ici on définit la classe PokemonFeu qui est une classe fille de la classe Pokemon
    def __init__(self,nom,niveau):
        super().__init__(nom,niveau,"feu",pv=80,attaque=45,defense=15)

class PokemonElectrique(Pokemon):
    def __init__(self,nom,niveau):
        super().__init__(nom,niveau,"electrique", pv=90,attaque=40,defense=25)

