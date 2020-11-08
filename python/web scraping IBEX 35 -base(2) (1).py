#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install beautifulsoup4


# In[3]:


pip install urllib3


# In[4]:


import urllib.request


# In[5]:


import csv
from datetime import datetime


# In[6]:


from bs4 import BeautifulSoup


# In[7]:


url= 'https://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'
IBEX35= urllib.request.urlopen(url)


# In[8]:


soup = BeautifulSoup(IBEX35, 'html.parser')


# In[9]:


print(soup.prettify())


# In[10]:


tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})
print(tabla.prettify())


# In[11]:


import numpy as np


# In[32]:


import time

def executeSomething():
    indices = []

    name=""
    price=""
    maximum=""
    minimum=""
    date=""
    nroFila=0
    for fila in tabla.find_all("tr"):
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==0:
                name=celda.text
                indice = {}
                indice['índice'] = name
            if nroCelda==2:
                price=celda.text
                indice['valor']=price
                indices.append(indice)
            if nroCelda==4:
                maximum = celda.text
                indice['máximo']= maximum
                indices.append(indice)
            if nroCelda==5:
                minimum = celda.text
                indice['mínimo']= minimum
                indices.append(indice)
                
          
            nroCelda=nroCelda+1
            with open('bolsa_ibex35.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([name, price, maximum, minimum])
    print (indices)
  
executeSomething()        


# In[ ]:





# In[ ]:




