#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import csv
import urllib.request ##importamos las herramientas necesarias 
from datetime import datetime
import time ##importamos la funcion tiempo para poner un reloj que descargue la indomacion cada 900 segundos 
##creamos una funcion que recogera la informacion 
def executeIBEX():
    url= 'https://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx' ##establecemos como nuestra url la pagina de la bolsa de madrid donde se muestra el resumnenes de indices del ibex 
    IBEX35 = urllib.request.urlopen(url) ##guardamos el acceso en la variable ibex35
    indices = [] ##creamos un array donde guardaremos la informacion 
    soup = BeautifulSoup(IBEX35, 'html.parser') ##print(soup.prettify()) ##usamos la funcion pretify para que sea mas humanamente legible 
    tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'}) ##buscamos donde esta el contenido llamado indices, y guardamos e tabla esta informacion 
    ##y volvemos a imprimir con pretify para ver si coincide con la informacion 
    name="" #definimos name y price maximo y minimo 
    price=""
    maximum=""
    minimum=""
    date=""
    nroFila=0 ##iniciamos el conctador 
    diaYhora = datetime.now() ##guardamos la fecha y hora de hoy 
    archivo="bolsa_ibex_35_"+str(diaYhora)+".csv"
    for fila in tabla.find_all("tr"): ##realizamos un for que recorra la tabla y busque las coincidencias con tr 
        nroCelda=0 ##iniciamos un contador 
        for celda in fila.find_all('td'): ##en el caso de todos tr que busque los td 
            if nroCelda==0: ##si el numero es 0, que es la posicion donde se encuentran los indicices le decimos que lo guarde e introduczca en el diccionario 
                name=celda.text
                indice = {}
                indice['indice'] = name
            if nroCelda==2: ##en el caso que sea 2 que es la posicion del valor. lo introducimos como valor 
                price=celda.text
                indice['valor']=price
                indices.append(indice)
            if nroCelda==4: ## en el caso que sea 4 que es la posicion del maximo, lo intrudicmos como maximo 
                maximum = celda.text
                indice['máximo']= maximum
                indices.append(indice)
            if nroCelda==5: ## en el caso que sea 5 que es la posicion del maximo, lo intrudicmos como minimo 
                minimum = celda.text
                indice['mínimo']= minimum
                indices.append(indice)
                
            nroCelda=nroCelda+1 ##sumamos uno a la celda 
            
        
            
         ##guardamos el nombre que tendra el archivo           
            
            with open(archivo, 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([name, price, maximum, minimum])
    print (indices) ##imprimimos el resultado para poder ver si lo hemos hecho correctamente 
    


    time.sleep(900) ## esto son los segundos entre una descarga y otra , realizamos cada 15 min que es el tiempo que se actualiza la pagina 

now = datetime.now()  ##establecemos la variable para saber la hora actual 
horaActual = now.strftime("%H:%M:%S") ##la pasamos a string y solo la hora los minutos y segundos 
horaCierre = "18:30:00" ##consideramos las 18:30 la hora del cierre de mercados 
while (horaActual<horaCierre): ##realizamos un bucle para que cada 15 min extraiga la informacion hasta que sean las 18:30
    
    executeIBEX()    ##llamamos la funcion   


# In[ ]:





# In[ ]:




