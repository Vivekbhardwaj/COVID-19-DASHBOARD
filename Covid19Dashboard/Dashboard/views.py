from django.shortcuts import render,HttpResponse


#Function to plot line curve for the cases/deaths due to COVID-19 with time
def plot(**kwargs) :
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    BASE=os.getcwd()
    df=pd.read_csv(os.path.join(BASE,'static','Dashboard','updated_with_cummulatives'))

    listOfCountries=list(set(df['countriesAndTerritories']))
    listOfCountries.sort()

    if len(kwargs['countries']) is 0 :
        return '',listOfCountries

    plt.figure(figsize=(15,8),dpi=100)
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
    plt.savefig(os.path.join(BASE,'static','Dashboard',country+'.png'))
    plt.close()

    return os.path.join('Dashboard',country+'.png'),listOfCountries




def index(request) :
    path=''
    listofCountries=[]
    if request.POST.get('country') is not None :
        path,listofCountries=plot(countries=[request.POST.get('country')],dailyDeaths= False,dailyCases= False,totalDeaths=True,totalCases=False)
        print(path)
        context={'countries':listofCountries,'path' : path}
        return render(request,'Dashboard/plottedGraph.html',context)

    else :
        path,listofCountries=plot(countries=[],dailyDeaths= False,dailyCases= False,totalDeaths=True,totalCases=False)
        path=''
    

    context={'countries':listofCountries,'path' : path}
    return render(request,'Dashboard/index.html',context)

