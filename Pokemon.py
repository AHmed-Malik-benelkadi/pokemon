import json
import random

class Pokemon:
    def __init__(self,nom,niveau,type_pokemon,pv=100,attaque=0,defense=0):
        self.__nom = nom
        self.niveau = niveau
        self.type_pokemon = type_pokemon
        self.__pv = pv
        self.attaque = attaque
        self.defense = defense

    def __str__(self):
        return f"{self.__nom} est de niveau {self.niveau} et est de type {self.type_pokemon}."

    def attaquer(self,adversaire):
        precision = random.randint(0,100)
        if precision <= 90:
            degats = self.attaque - adversaire.defense
            if degats < 0:
                degats = 0
            adversaire.__pv -= degats
            print(f"{self.__nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
            if adversaire.pv <= 0:
                print(f"{adversaire.nom} est K.O.")
                return self.__nom
        else:
            print(f"{self.__nom} attaque {adversaire.nom} et rate son attaque.")

    def get_nom(self):
        return self.__nom
    def get_pv(self):
        return self.__pv

    def set_pv(self, pv):
        self.__pv = pv

    def set_nom(self, nom):
        self.__nom = nom
class PokemonNormal(Pokemon):
    def __init__(self,nom,niveau):
        super().__init__(nom,niveau,"normal",pv=100,attaque=10,defense=10)


class PokemonEau(Pokemon):
    def __init__(self, nom, attaque):
        super().__init__(nom, 100, attaque, 0, "Eau")
        self._Pokemon__pv = 100

    def get_pv(self):
        return self._Pokemon__pv


class PokemonFeu(Pokemon):
    def __init__(self,nom,niveau):
        super().__init__(nom,niveau,"feu",pv=80,attaque=45,defense=15)

class PokemonElectrique(Pokemon):
    def __init__(self,nom,niveau):
        super().__init__(nom,niveau,"electrique", pv=90,attaque=40,defense=25)


