import pandas as pd
from comparison import similarity
from comprobar_vida import check_life
from distancias import Distancias
from conseguir_url import link

df = pd.read_csv('data.csv')
planeta = input('Enter the name of the planet: ')

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

distancia = get_float_input('Enter the distance of the planet to its star (in AU): ')
masa_sol = get_float_input('Enter the mass of the star (in Suns): ')
temperatura = get_float_input('Enter the equilibrium temperature of the planet (in °C): ') + 273.15
masa_planeta = get_float_input('Enter the mass of the planet (in Earths): ')
radio_planeta = get_float_input('Enter the radius of the planet (in Earths): ')
values = [radio_planeta, masa_planeta, temperatura, masa_sol, distancia]

planeta_parecido = similarity(df, values)
print('The most similar planet is: ', planeta_parecido['pl_name'])
print('Is it habitable? ', check_life(planeta_parecido['pl_orbsmax'], planeta_parecido['st_mass'], planeta_parecido['pl_eqt']))

distanciaNave = Distancias(planeta_parecido["sy_dist"])
print('The travel time with a Star Trek ship to the planet is: ', distanciaNave.starTrek(), 'years')
print('The travel time with a Star Wars ship to the planet is: ', distanciaNave.starWars(), 'years')
print('The travel time with a Space Odyssey ship to the planet is: ', distanciaNave.SpaceOdyssey(), 'years')
print('The travel time with a Halo ship to the planet is: ', distanciaNave.halo(), 'years')

print(f'For more information about the planet: "{planeta_parecido["pl_name"]}", visit: {link(planeta_parecido["pl_name"])}')
