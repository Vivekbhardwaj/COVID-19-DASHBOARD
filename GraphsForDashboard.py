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
import os

#reading the csv
df=pd.read_csv('covid data')

#list of countries in data
listOfCountries=list(set(df['countriesAndTerritories']))
listOfCountries.sort()

#adding some extra columns for visualization purpose
cummulativeDeaths=[]
cummulativeCases=[]

for country in listOfCountries :
    temp=df.loc[df['countriesAndTerritories']==country]
    temp=temp[::-1]
    l = [(x,y) for x, y in zip(temp['deaths'], temp['cases'])]
    cum_deaths=[l[0][0]]
    cum_cases=[l[0][1]]
    for index in range(1,len(l),1) :
        cum_deaths.append(cum_deaths[len(cum_deaths)-1]+l[index][0])
        cum_cases.append(cum_cases[len(cum_cases)-1]+l[index][1])
    cum_deaths.reverse()
    cum_cases.reverse()
    cummulativeDeaths.extend(cum_deaths)
    cummulativeCases.extend(cum_cases)
    

df['Cummulative Deaths'] = cummulativeDeaths
df['Cummulative Cases'] = cummulativeCases




def plot(**kwargs) :
    plt.figure(figsize=(50,35),dpi=100)
    plt.title('Deaths/Cases due to covid-19 on a daily basis')
    for country in kwargs['countries'] :
        temp=df.loc[df['countriesAndTerritories']==country]
        temp=temp[::-1]
        if kwargs['dailyDeaths'] :
            plt.plot(temp['dateRep'],temp['deaths'],'*-',label='Deaths in '+country+' on daily basis')
        if kwargs['dailyCases'] :
            plt.plot(temp['dateRep'],temp['cases'],'--',label='Cases in '+country+' on daily basis ')
        if kwargs['totalDeaths'] :
            plt.plot(temp['dateRep'],temp['Cummulative Deaths'],'.-',label='Total Deaths in '+country)
        if kwargs['totalCases'] :
            plt.plot(temp['dateRep'],temp['Cummulative Cases'],'.--',label='Total Cases in '+country)

    temp=df.loc[df['countriesAndTerritories']==kwargs['countries'][0]]
    date=temp['dateRep']
    date=date[::13]
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Deaths/Cases')
    plt.legend()
    # plt.savefig(os.path.join(os.getcwd(),'DeathsInAllCountriesVisualized',country+'.png'))
    plt.show()
    plt.close()             #Close the figure because else it stays in memory and memory limit exceeds while rendering



# To save graphs of all countries
# for index in range(104,len(listOfCountries)) :
#     plot(countries=[listOfCountries[index]],dailyDeaths=False,dailyCases=False,totalDeaths=True,totalCases=False)
#     continue


while(True) :
    countries = input('Enter the country name you want to see stastics : \n').split()
    neededInsights=list(map(int,input('Choose the needed insights by typing the all needed numbers with space seperation \n'+
    '1)Deaths On a Daily Basis\n'+ 
    '2)Cases encountered on daily basis\n'+
    '3)Total Deaths with time\n'+
    '4)Total cases with time\n').split()))

    plot(countries=countries,dailyDeaths=1 in neededInsights,dailyCases=2 in neededInsights,totalDeaths=3 in neededInsights,totalCases=4 in neededInsights)





