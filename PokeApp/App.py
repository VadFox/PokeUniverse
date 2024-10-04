import random
import pokebase as pb



Number = random.randint(1,200)

chesto = pb.APIResource('berry', 'chesto')
# print(chesto.name)

charmander = pb.pokemon('charmander')
# print(charmander.height)

pk = pb.SpriteResource('pokemon', 6)

# print(pk.url)


PokemonRandom = pb.pokemon(Number)
PokemonImg = pb.SpriteResource('pokemon',Number)

print(PokemonRandom, PokemonImg.url)





