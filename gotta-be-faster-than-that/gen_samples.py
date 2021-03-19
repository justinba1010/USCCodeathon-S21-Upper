#! /usr/bin/env python3

import numpy as np
from sys import stdout
import string
import os
from tqdm import tqdm

rng = np.random.default_rng(42)

pokedex = ['Squirtle'] + list(rng.permutation([
  'Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard',
  'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto',
  'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew',
  'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix',
  'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect',
  'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape',
  'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke',
  'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem',
  'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Farfetchd',
  'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar',
  'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone',
  'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela',
  'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar',
  'Pinsir', 'Tauros', 'Claydol', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon',
  'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini',
  'Dragonair', 'Dragonite', 'Mewtwo', 'Mew', 'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion',
  'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak',
  'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu',
  'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom',
  'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking',
  'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull',
  'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo',
  'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom',
  'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid',
  'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho-oh',
  'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert',
  'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad',
  'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia',
  'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask',
  'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty',
  'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun',
  'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt',
  'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria',
  'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy'
]))

def int_to_name(n, alphabet=string.ascii_letters, max_n=len(pokedex)):
  if max_n < len(pokedex):
    return pokedex[n]  # Use pokedex if there are enough pokemons

  m = len(alphabet)
  base_m = [] if n > 0 else [0]
  while n > 0:
    base_m.append(n % m)
    n //= m
  s = "".join(alphabet[i] for i in reversed(base_m))
  return s

def generate_sample(n, k, l, file=stdout):
  n -= n % np.lcm(k,l)  # Ensure n is divisible by k and l

  kl = rng.choice([k,l])
  shuffled_groups = rng.permutation(n)  # Each contiguous segment of kl elements is a group
  shuffled_idxs   = rng.permutation(n)  # Order of indices to put into the graph

  print(n, k, l, file=file)  # First line has problem info

  for i in tqdm(shuffled_idxs):
    j = i + 1 if (i + 1) % kl > 0 else i - kl + 1
    i, j = rng.permutation([i, j])  # Flip the order of the pair
    print(int_to_name(shuffled_groups[i], max_n=n), int_to_name(shuffled_groups[j], max_n=n), file=file)

  return kl

def generate_multiple(min_exp=2, max_exp=11, k_max=10, exp_base=5):
  ns = [exp_base**i for i in range(min_exp,max_exp+1)]
  ks = list(range(3, k_max+1))

  os.system("mkdir -p testcases/input testcases/output")
  for i, n in enumerate(ns):
    ifname = "testcases/input/input%02d.txt" % i
    ofname = "testcases/output/output%02d.txt" % i

    k = rng.choice(ks)
    l = rng.choice([k_ for k_ in ks if k_ != k])

    print("Test %02d: %d (%d, %d)" % (i, n, k, l))

    with open(ifname, "w+") as ifile, open(ofname, "w+") as ofile:
      cycle_size = generate_sample(n, k, l, file=ifile)
      print(cycle_size, file=ofile)

def test_one(n, k, l):
  from profile_solution import main_limited

  with open("/tmp/sampleinput.txt", "w+") as f, open("/tmp/sampleoutput.txt", "w+") as of:
    print("Generating sample (%d, %d, %d)" % (n,k,l))
    cycle_size = generate_sample(n, k, l, file=f)
    print(cycle_size, file=of)
    f.seek(0)
    success, output = main_limited(f=f)
    if output != cycle_size:
      print("WRONG ANSWER: Correct %d, Given %d" % (cycle_size, output))
      success = False
    return success

def main():
  generate_multiple()

if __name__ == "__main__":
  main()
