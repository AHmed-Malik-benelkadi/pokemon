from Pokedex import *
from Pokemon import *
import random
import json

class Combat:
    def __init__(self, pokemon1, pokemon2, pokedex):
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2
        self.__pokedex = pokedex
        self.__tour = 1

    def est_finie(self):
        if self.__pokemon1.get_pv() <= 0 or self.__pokemon2.get_pv() <= 0:
            return True
        else:
            return False

    def get_vainqueur(self):
        if self.__pokemon1.get_pv() <= 0:
            return self.__pokemon2.get_nom()
        elif self.__pokemon2.get_pv() <= 0:
            return self.__pokemon1.get_nom()
        else:
            return None

    def attaque_possible(self):
        return random.randint(0, 1)

    def calculer_degats(self, attaquant, defenseur):
        TABLE_TYPES = []

        for types, multiplicateur in TABLE_TYPES:
            if attaquant.type_pokemon in types and defenseur.type_pokemon in types:
                multiplicateur_type = multiplicateur
                break
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
        while not self.est_finie():
            print(f"Tour {self.__tour}")
            if self.attaque_possible():
                print(f"{self.__pokemon1.get_nom()} attaque {self.__pokemon2.get_nom()}")
                degats = self.calculer_degats(self.__pokemon1, self.__pokemon2)
                self.enlever_pv(self.__pokemon2, degats)
            else:
                print(f"{self.__pokemon2.get_nom()} attaque {self.__pokemon1.get_nom()}")
                degats = self.calculer_degats(self.__pokemon2, self.__pokemon1)
                self.enlever_pv(self.__pokemon1, degats)
            self.__tour += 1
        print(f"Le combat est terminé ! Le vainqueur est {self.get_vainqueur()} !")
        vainqueur = self.get_vainqueur()
        if vainqueur is not None:
            pokemon_vainqueur = self.__pokedex.get_pokemon()
            if pokemon_vainqueur is None:
                # Si le Pokémon n'existe pas dans le Pokedex, on le crée
                pokemon_vainqueur = eval(vainqueur + "()")
                self.__pokedex.ajouter_pokemon(pokemon_vainqueur)
            else:
                # Find the correct Pokemon instance in the list
                for pokemon in pokemon_vainqueur:
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



