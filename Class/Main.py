import random
import json
from Combat import *
from Pokemon import *
from Pokedex import *

def ajouter_pokemon():
    nom = input("Nom du Pokemon : ")
    type = input("Type du Pokemon : ")
    pv = int(input("Points de vie du Pokemon : "))
    attaque = int(input("Puissance d'attaque du Pokemon : "))
    defense = int(input("Defense du Pokemon : "))
    pokemon = Pokemon(nom, pv, attaque, defense, type)
    pokedex = Pokedex()
    pokedex.ajouter_pokemon(pokemon)
    print(f"{nom} a été ajouté au Pokédex.")


def lancer_partie():
    pokedex = Pokedex()
    with open("pokedex.json", "r") as f:
        pokemons_json = json.load(f)
        pokemons = []
        for pokemon_dict in pokemons_json:
            if pokemon_dict["type_pokemon"] == "Normal":
                pokemon = PokemonNormal(pokemon_dict["nom"], 1)
            elif pokemon_dict["type_pokemon"] == "Feu":
                pokemon = PokemonFeu(pokemon_dict["nom"], 1)
            elif pokemon_dict["type_pokemon"] == "Eau":
                pokemon = PokemonEau(pokemon_dict["nom"], 1)
            elif pokemon_dict["type_pokemon"] == "Electrique":
                pokemon = PokemonElectrique(pokemon_dict["nom"], 1)
            else:
                pokemon = Pokemon(pokemon_dict["nom"], 1, pokemon_dict["type_pokemon"], pokemon_dict["pv"],
                                  pokemon_dict["attaque"], pokemon_dict["defense"])
            pokemons.append(pokemon)


    print("Liste des Pokémon disponibles :")
    for i, pokemon in enumerate(pokemons):
        print(f"{i+1}. {pokemon.get_nom()} ({pokemon.type_pokemon})")
    choix = int(input("Entrez le numéro du Pokémon avec lequel vous voulez jouer : ")) - 1
    joueur = pokemons[choix]
    adversaires = [p for p in pokemons if p != joueur]
    adversaire = random.choice(adversaires)
    combat = Combat(joueur, adversaire, pokedex)
    combat.lancer_combat()


def afficher_pokedex():
    pokedex = Pokedex()
    pokedex.afficher_pokedex()

while True:
    print("Menu :")
    print("1. Lancer une partie")
    print("2. Ajouter un Pokémon")
    print("3. Afficher le Pokédex")
    choix = input("Entrez votre choix : ")
    if choix == "1":
        lancer_partie()
    elif choix == "2":
        ajouter_pokemon()
    elif choix == "3":
        afficher_pokedex()
    else:
        break
