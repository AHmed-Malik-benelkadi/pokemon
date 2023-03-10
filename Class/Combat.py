from Pokedex import *
from Pokemon import *
import random
import json

class Combat:
    """Classe représentant un combat entre deux Pokémon
    Attributs :
        - pokemon1 : le premier Pokémon
        - pokemon2 : le second Pokémon
        - pokedex : le Pokédex
        """
    def __init__(self, pokemon1, pokemon2, pokedex):
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2
        self.__pokedex = pokedex
        self.__tour = 1

    def fini(self):
        if self.__pokemon1.get_pv() <= 0 or self.__pokemon2.get_pv() <= 0:  # Si un des deux Pokémon est K.O. le combat est terminé
            return True # Le combat est terminé
        else:
            return False # Le combat n'est pas terminé

    def get_vainqueur(self): # Renvoie le nom du vainqueur
        if self.__pokemon1.get_pv() <= 0: # Si le Pokémon 1 est K.O. le Pokémon 2 est le vainqueur
            return self.__pokemon2.get_nom()  # Renvoie le nom du Pokémon 2
        elif self.__pokemon2.get_pv() <= 0: # Si le Pokémon 2 est K.O. le Pokémon 1 est le vainqueur
            return self.__pokemon1.get_nom() # Renvoie le nom du Pokémon 1
        else:
            return None

    def attaque_possible(self): # Renvoie True si le Pokémon 1 attaque, False si le Pokémon 2 attaque
        return random.randint(0, 1)

    def calculer_degats(self, attaquant, defenseur): # Calcul les dégâts infligés par le Pokémon attaquant au Pokémon défenseur
        TABLE_TYPES = []

        i = 0
        found = False
        while i < len(TABLE_TYPES) and not found:
            types, multiplicateur = TABLE_TYPES[i]
            if attaquant.type_pokemon in types and defenseur.type_pokemon in types:
                multiplicateur_type = multiplicateur
                found = True
            i += 1
        else:
            multiplicateur_type = 1

        degats = int(multiplicateur_type * attaquant.attaque - defenseur.defense)
        return degats if degats > 0 else 1

    def enlever_pv(self, pokemon, degats):
        pokemon.set_pv(pokemon.get_pv() - degats)
        if pokemon.get_pv() <= 0:
            print(f"{pokemon.get_nom()} est K.O. !")
        else:
            print(f"{pokemon.get_nom()} a {pokemon.get_pv()} PV.")

    def lancer_combat(self):
        print(f"Le combat entre {self.__pokemon1.get_nom()} et {self.__pokemon2.get_nom()} commence !")
        while not self.fini(): # Tant que le combat n'est pas terminé on continue
            print(f"Tour {self.__tour}") # On affiche le numéro du tour
            if self.attaque_possible(): # Si le Pokémon 1 attaque
                print(f"{self.__pokemon1.get_nom()} attaque {self.__pokemon2.get_nom()}") # On affiche le nom du Pokémon 1 et du Pokémon 2
                degats = self.calculer_degats(self.__pokemon1, self.__pokemon2)
                self.enlever_pv(self.__pokemon2, degats)
            else:
                print(f"{self.__pokemon2.get_nom()} attaque {self.__pokemon1.get_nom()}")
                degats = self.calculer_degats(self.__pokemon2, self.__pokemon1)
                self.enlever_pv(self.__pokemon1, degats)
            self.__tour += 1 # On incrémente le numéro du tour
        print(f"Le combat est terminé ! Le vainqueur est {self.get_vainqueur()} !")
        vainqueur = self.get_vainqueur()
        if vainqueur is not None: # Si le vainqueur n'est pas None
            pokemon_vainqueur = self.__pokedex.get_pokemon()
            if pokemon_vainqueur is None:
                # Si le Pokémon n'existe pas dans le Pokedex, on le crée
                pokemon_vainqueur = eval(vainqueur + "()")
                self.__pokedex.ajouter_pokemon(pokemon_vainqueur)
            else:
                for pokemon in pokemon_vainqueur: # Sinon on incrémente le nombre de victoires du Pokémon
                    if pokemon.nom == vainqueur:
                        # Update the number of victories
                        pokemon.set_nb_victoires(pokemon.get_nb_victoires() + 1)
                        break

            self.__pokedex.sauvegarder_pokedex('pokemon.json')


pikachu = PokemonElectrique("Pikachu", 10)
Salameche = PokemonFeu("Salameche", 10)
pokedex = Pokedex()


combat = Combat(pikachu, Salameche, pokedex)
combat.lancer_combat()

pokedex.afficher_pokedex()



