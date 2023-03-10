import json
import random
from Pokemon import *

class Pokedex():
    def __init__(self):
        self.__pokemon = []
        self.__nom_pokemon = []

    def ajouter_pokemon(self,pokemon):
        if pokemon.get_nom() not in self.__nom_pokemon:
            self.__pokemon.append(pokemon)
            self.__nom_pokemon.append(pokemon.get_nom())
            print(f"{pokemon.get_nom()} a été ajouté au Pokédex.")

        else:
            print(f"{pokemon.get_nom()} est déjà dans le Pokédex.")

    def get_pokemon(self):
        return self.__pokemon
    def get_nom_pokemon(self):
        return self.__nom_pokemon

    def set_pokemon(self,pokemon):
        self.__pokemon = pokemon
    def set_nom_pokemon(self,nom_pokemon):
        self.__nom_pokemon = nom_pokemon

    def afficher_pokedex(self):
        print("Pokédex :")
        for pokemon in self.__pokemon:
            print(pokemon)
        print(f"Nombre de Pokémon dans le Pokédex : {len(self.__pokemon)}")

    def sauvegarder_pokedex(self,fichier):
        with open(fichier,"w") as f :
            pokemon_json =[]
            for pokemon in self.__pokemon:
                pokemon_dict = {"nom":pokemon.get_nom(),"niveau":pokemon.niveau,"type_pokemon":pokemon.type_pokemon,"pv":pokemon.get_pv(),"attaque":pokemon.attaque,"defense":pokemon.defense}
                pokemon_json.append(pokemon_dict)
            json.dump(pokemon_json,f,indent=4)
        print(f"Le Pokédex a été sauvegardé dans le fichier {fichier}.")

    def charger_pokedex(self,fichier):
        with open(fichier,"r") as f:
            pokemon_json = json.load(f)
            for pokemon_dict in pokemon_json:
                if pokemon_dict["nom"] not in self.__nom_pokemon:
                    if pokemon_dict["type"] == "Normal":
                        pokemon = PokemonNormal(pokemon_dict["nom"], 1)
                    elif pokemon_dict["type"] == "Feu":
                        pokemon = PokemonFeu(pokemon_dict["nom"], 1)
                    elif pokemon_dict["type"] == "Eau":
                        pokemon = PokemonEau(pokemon_dict["nom"], 1)
                    elif pokemon_dict["type"] == "Electrique":
                        pokemon = PokemonElectrique(pokemon_dict["nom"], 1)
                    else:
                        pokemon = Pokemon(pokemon_dict["nom"], 1, pokemon_dict["type"], pokemon_dict["pv"],
                                          pokemon_dict["attaque"], pokemon_dict["defense"])
                    self.__pokemons.append(pokemon)
                    self.__noms_pokemons.append(pokemon.get_nom())
                    print(f"{pokemon.get_nom()} a été ajouté au Pokédex.")
                else:
                    print(f"{pokemon_dict['nom']} est déjà dans le Pokédex.")



    def __str__(self):
        return f"Le Pokédex contient {len(self.__pokemon)} Pokémon."



if __name__ == "__main__":
    pokedex = Pokedex()
    pokedex.ajouter_pokemon(PokemonNormal("Pikachu",1))
    pokedex.ajouter_pokemon(PokemonFeu("Salameche",1))
    pokedex.ajouter_pokemon(PokemonEau("Carapuce",1))
    pokedex.ajouter_pokemon(PokemonElectrique("Pikachu",1))
    pokedex.afficher_pokedex()
    pokedex.sauvegarder_pokedex("pokedex.json")
    pokedex.charger_pokedex("pokedex.json")
    pokedex.afficher_pokedex()