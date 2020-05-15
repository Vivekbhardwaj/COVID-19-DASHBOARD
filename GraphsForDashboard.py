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

df=pd.read_csv('covid data')
countries=set(df['countriesAndTerritories'])
plt.figure(figsize=(500,350),dpi=100)
plt.title('Deaths due to covid 19')
for country in countries :
    temp=df.loc[df['countriesAndTerritories']==country]
    plt.plot(temp['dateRep'],temp['deaths'],label=country)
plt.legend()
plt.xlabel('Date')
plt.ylabel('Deaths')
# plt.show()
plt.savefig('Deaths plot',dpi=100)




