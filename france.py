import pandas as pd
from pandas.core.arrays.sparse import dtype

#wrapping the whole script in a function to call from plan.R
# source: https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/, note source file is semicolon-delimeted

def france():

    source_url = 'https://www.data.gouv.fr/fr/datasets/r/fa4ad329-14ec-4394-85a4-c5df33769dff'

    #colunns and datatypes
    input_columns = ['fra','jour', 'n_cum_dose1','n_cum_complet']
    output_columns = {'fra': 'code', 'jour' : 'date', 'n_cum_dose1' : 'people_vaccinated', 'n_cum_complet' : 'people_fully_vaccinated'}
    output_column_dtypes = {'code': 'str', 'vaccinations' : 'int', 'people_vaccinated' : 'int', 'people_fully_vaccinated' : 'int'}

    #import data and parse dates
    france_vax = pd.read_csv(source_url, delimiter=";", usecols = input_columns, parse_dates=['jour'])

    #rename columns to match latest.csv format
    france_vax.rename(columns = output_columns, inplace=True)

    #get total vaccinations from cumulative figures
    france_vax["vaccinations"] = france_vax["people_vaccinated"]+france_vax["people_fully_vaccinated"]

    #update country code to match output format
    france_vax["code"] = 'FRA'

    #confirm dtypes
    france_vax = france_vax.astype(output_column_dtypes)

    return france_vax



