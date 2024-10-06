# Descripción: Este archivo contiene la función que calcula la similitud entre la entrada del usuario y los exoplanetas en la base de datos.
import pandas as pd
from scipy.spatial.distance import euclidean

def similarity(df, values):
    # if column not num -> fill with 0
    df[['pl_rade', 'pl_bmasse', 'pl_eqt', 'st_mass', 'pl_orbsmax']] = df[['pl_rade', 'pl_bmasse', 'pl_eqt', 'st_mass', 'pl_orbsmax']].apply(pd.to_numeric, errors='coerce').fillna(0)

    # calculate with each roww
    df['resultDistance'] = df[['pl_rade', 'pl_bmasse', 'pl_eqt', 'st_mass', 'pl_orbsmax']].apply(lambda row: euclidean(row, values), axis=1)

    # min distance
    mostCompatible = df['resultDistance'].idxmin()
    exoplanet = df.iloc[mostCompatible]
    return exoplanet

