# Data source : https://www.ecdc.europa.eu
# import requests
# import io
# url='https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
# s=requests.get(url).content
# c=pd.read_csv(io.StringIO(s.decode('utf-8')))
# c.head()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading the csv
df=pd.read_csv('covid data')
listOfCountries=list(set(df['countriesAndTerritories']))


def plot(*args) :
    plt.figure(figsize=(50,35),dpi=100)
    plt.title('Deaths/Cases due to covid-19 on a daily basis')
    for country in args[0] :
        temp=df.loc[df['countriesAndTerritories']==country]
        temp=temp[::-1]
        plt.plot(temp['dateRep'],temp['deaths'],label='Deaths in '+country)
        plt.plot(temp['dateRep'],temp['cases'],'--',label='Cases in '+country)

    temp=df.loc[df['countriesAndTerritories']==args[0][0]]
    date=temp['dateRep']
    date=date[::13]
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Deaths')
    plt.legend()
    plt.show()

while(True) : 
    countries = input('Enter the country name you want to see stastics : \n').split()
    plot(countries)





