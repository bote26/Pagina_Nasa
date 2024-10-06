import streamlit as st
import pandas as pd
import scipy
from comparison import similarity
from comprobar_vida import check_life
from distancias import Distancias
from conseguir_url import link
from consultar_chat import consultar_chatgpt
import numpy as np
from datetime import timedelta


@st.cache_data
def load_data():
    return pd.read_csv('data.csv')
df = load_data()
st.title("Create your own exoplanet ")
st.markdown('''Exoplanets are planets outside our solar sistem, they are very interesting to study and there are many of them.
            Some of them can even have life on them!''')
st.markdown('''This is a simple web app that helps you find an exoplanet similar to the one you want to create.''')

st.markdown('''To do this, you need to provide some information about the exoplanet you want to create.
            This information includes the distance of the planet to its star, the mass of the star, the temperature of the planet, the mass of the planet and the radius of the planet.''')

st.markdown("Once you provide this information, the app will find the exoplanet in the NASA database that is most similar to the one you want to create. ")

st.subheader("Let's get started!")
st.write("Enter the information about the exoplanet you want to create in the sidebar.")

st.sidebar.write("Distance of the planet to its star (in AU):")
distance = st.sidebar.slider('', min_value=0.1, max_value=10.0, value=0.1, step=0.1, key='distance')
st.sidebar.write("Mass of the star (in Solar masses):")
mass_star = st.sidebar.slider('', min_value=0.1, max_value=2.0, value=0.1, step=0.1, key='mass_star')
st.sidebar.write("Temperature of the planet (in °C):")
temperature = st.sidebar.slider('', min_value=-200, max_value=1000, value=-200, step=10, key='temperature')
st.sidebar.write("Mass of the planet (in Earth masses):")
mass_planet = st.sidebar.slider('', min_value=0.1, max_value=5.0, value=0.1, step=0.1, key='mass_planet')
st.sidebar.write("Radius of the planet (in Earth radius):")
radius_planet = st.sidebar.slider('', min_value=0.1, max_value=5.0, value=0.1, step=0.1, key='radius_planet')

values = [radius_planet, mass_planet, temperature+273.15, mass_star, distance]
planeta_parecido = similarity(df, values)
st.write('The most similar planet is: ', planeta_parecido['pl_name'])
st.write('Is it habitable? ', "Yes" if check_life(planeta_parecido['pl_orbsmax'], planeta_parecido['st_mass'], planeta_parecido['pl_eqt']) else "No")

distanciaNave = Distancias(planeta_parecido["sy_dist"])
years_to_days = lambda years: years * 365.25

st.write('The travel time with a Star Trek ship to the planet is: ', distanciaNave.starTrek(), 'years')
st.write('The travel time with a Star Wars ship to the planet is: ', distanciaNave.starWars(), 'years')
st.write('The travel time with a Space Odyssey ship to the planet is: ', distanciaNave.SpaceOdyssey(), 'years')
st.write('The travel time with a Halo ship to the planet is: ', distanciaNave.halo(), 'years')

st.write(f'For more information about the planet: "{planeta_parecido["pl_name"]}", visit: {link(planeta_parecido["pl_name"])}')
