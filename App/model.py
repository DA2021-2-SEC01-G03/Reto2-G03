
from DISClib.DataStructures.arraylist import isPresent
from DISClib.DataStructures.chaininghashtable import keySet, valueSet
import config as cf
import operator
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.ADT import map 
assert cf

# Construccion de modelos

def newCatalog():
   
    catalog = {'artists': None,
               'artworks': None,
               'Medium': None,
               'Nationality': None,
               'Department': None
               }

    catalog['artists'] = map.newMap(maptype='PROBING', numelements= 30000, loadfactor= 0.5)
    catalog['artworks'] = map.newMap(maptype='PROBING', numelements= 280000, loadfactor= 0.5)
    catalog['Medium'] = map.newMap(maptype= 'PROBING', numelements= 280000, loadfactor= 0.5)
    catalog['Nationality'] = map.newMap(maptype= 'PROBING', numelements= 280000, loadfactor= 0.5)
    catalog['Department'] = map.newMap(maptype= 'PROBING', numelements= 280000, loadfactor= 0.5)
   
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    map.put(catalog['artists'], artist['ConstituentID'], artist)
    
     
def addArtwork(catalog, artwork):
    map.put(catalog['artworks'], artwork['ObjectID'], artwork)
    constituents = artwork['ConstituentID'][1:][:-1].split(",")
    artwork['Constituents'] = constituents   


def loadArtistsNames(catalog):
    artworks = catalog['artworks']
    artists = catalog['artists']
    listArtworks = map.keySet(artworks)
    for key in lt.iterator(listArtworks):
        artwork = map.get(artworks, key)['value']
        constituents = artwork['Constituents']
        artwork['ArtistsNames'] = []
        artwork['Nationality'] = []        
        tamConstituents = len(constituents)
        i = 0
        while i < tamConstituents:
           artist = map.get(artists, constituents[i])
           if artist == None:
              artwork['ArtistsNames'] = []
              artwork['Nationality'] = []  
           else:   
              artwork['ArtistsNames'].append(artist['value']['DisplayName'])   
              artwork['Nationality'].append(artist['value']['Nationality'])  
           i += 1 


def addMedium(catalog, artwork):
    Map = catalog['Medium']
    if map.contains(Map, artwork['Medium']):
      bucket = map.get(Map, artwork['Medium'])['value']
      lt.addLast(bucket, artwork)
      map.put(Map, artwork['Medium'], bucket)
    else:     
      bucket = lt.newList('ARRAY_LIST')  
      lt.addLast(bucket, artwork)      
      map.put(Map, artwork['Medium'], bucket)


def addDepartment(catalog, artwork):
    Map = catalog['Department']   
    if map.contains(Map, artwork['Department']):
      bucket = map.get(Map, artwork['Department'])['value']
      lt.addLast(bucket, artwork)
      map.put(Map, artwork['Department'], bucket)
    else:     
      bucket = lt.newList('ARRAY_LIST')  
      lt.addLast(bucket, artwork)      
      map.put(Map, artwork['Department'], bucket)

           
def loadNationalities(catalog):
    mapNationality = catalog['Nationality']
    artworks = catalog['artworks']
    listArtworks = map.keySet(artworks)
    for key in lt.iterator(listArtworks):
        artwork = map.get(artworks, key)['value']
        nationalities = artwork['Nationality']
        tamNationalities = len(nationalities)
        i = 0
        while i < tamNationalities:
            if map.contains(mapNationality, nationalities[i]):
              bucket = map.get(mapNationality, nationalities[i])['value']
              lt.addLast(bucket, artwork)
              map.put(mapNationality, nationalities[i], bucket)
            else:  
              bucket = lt.newList('ARRAY_LIST') 
              lt.addLast(bucket, artwork) 
              map.put(mapNationality, nationalities[i], bucket)
            i += 1
    

    



# Funciones para creacion de datos

# Funciones de consulta

def artistsByDates(catalog, date1:int, date2:int):
    list = lt.newList('ARRAY_LIST')
    artists = catalog['artists']
    i = 1
    values = map.valueSet(artists)
    count = 1
    for artist in lt.iterator(values):
       if (int(artist['BeginDate']) >= date1) and (int(artist['BeginDate']) <= date2):
          lt.addLast(list, artist)
          count += 1
       i += 1
     
    return (list,count)



def artworksByDates(catalog, date1, date2):
    list = lt.newList('ARRAY_LIST')
    artworks = catalog['artworks']
    values = map.valueSet(artworks)
    count = 0
    for artwork in lt.iterator(values):
      DateInt = becomeDateAquiredToInt(artwork['DateAcquired'])
      if DateInt > date1 and DateInt < date2:
         lt.addLast(list, artwork)
         count += 1           
    return (list,count)               



def artworkArtistByTechnique(catalog,artistName):
    idArtist = ""
    countPieces = 0
    countTechnique = 0
    counter = map.newMap()
    
    artists = map.valueSet(catalog['artists'])
    for artist in lt.iterator(artists):
        if artist['DisplayName'] == artistName:
           idArtist = artist['ConstituentID'] 
           break

    artworks = map.valueSet(catalog['artworks'])
    for artwork in lt.iterator(artworks):
        if artistName in artwork['ArtistsNames']:
            technique = artwork['Medium']
            if map.contains(counter, technique):
                newValue = map.get(counter, technique)['value']
                newValue['Number of artworks'] += 1
                map.put(counter, technique, newValue)
                countPieces += 1
            else:
                newValue = {'technique': technique, 'Number of artworks': 1}
                map.put(counter, technique, newValue)
                countTechnique += 1
                countPieces += 1

    list = map.valueSet(counter)            
           
          
    return list,idArtist,countPieces,countTechnique



def artworksByNationality(catalog):
    list = lt.newList('ARRAY_LIST')
    nationalities = catalog['Nationality']
    listNationalities = map.keySet(nationalities)
    for nationality in lt.iterator(listNationalities):
        artworks = map.get(nationalities, nationality)['value']
        amount = lt.size(artworks)
        value = {'Nationality': nationality, 'Count': amount}
        lt.addLast(list, value)

    return list    



def artworksOfNacionality(catalog,Nationality):
    listNationality = map.get(catalog['Nationality'], Nationality)['value']

    return listNationality        



def transportCostByDepartment(catalog,department):
    departmentList = map.get(catalog['Department'], department)['value']
    costsSum = 0
    weightsSum = 0 
    costKg = 0
    costM2 = 0
    costM3 = 0 
    
    for artwork in lt.iterator(departmentList):
        if artwork['Weight (kg)'] != '0' and artwork['Weight (kg)'] != '':
           costKg = 72.00 / float(artwork['Weight (kg)'])
           weightsSum += costKg
        if artwork['Height (cm)'] != '0' and artwork['Height (cm)'] != '' and artwork['Width (cm)'] != '0' and artwork['Width (cm)'] != '':  
           costM2 = 72.00 / (float(artwork['Height (cm)'])/100 * float(artwork['Width (cm)'])/100)
        if artwork['Height (cm)'] != '0' and artwork['Height (cm)'] != '' and artwork['Width (cm)'] != '0' and artwork['Width (cm)'] != '' and artwork['Length (cm)'] != '0' and artwork['Length (cm)'] != '':   
           costM3 = 72.00 / (float(artwork['Height (cm)'])/100 * float(artwork['Width (cm)'])/100 * float(artwork['Length (cm)'])/100)

        list = [costKg,costM2,costM3]
        maxCost = max(list)
        if maxCost <= 0:
            finalCost = 48
        else:
            finalCost = maxCost

        artwork['cost'] = finalCost
        costsSum += finalCost
                         

    return (departmentList,costsSum,weightsSum)


# Funciones utilizadas para comparar elementos dentro de una lista

def compareBeginDates(artist1, artist2):
    return int(artist1['BeginDate']) < int(artist2['BeginDate'])

def compareDatesAquired(artwork1, artwork2):
    date1 = artwork1['DateAcquired']
    date2 = artwork2['DateAcquired']

    intDate1 = becomeDateAquiredToInt(date1)
    intDate2 = becomeDateAquiredToInt(date2)

    return intDate1 < intDate2

def compareTechnique(technique1, technique2):
    return int(technique1['Number of artworks']) > int(technique2['Number of artworks'])

def compareNationalities(nationality1, nationality2):
    return int(nationality1['Count']) > int(nationality2['Count'])    

def compareCost(artwork1,artwork2):
    return int(artwork1['cost']) < int(artwork2['cost'])    

def compareDate(artwork1,artwork2):
    
    if artwork1['Date'] == "" or len(artwork1['Date']) > 4:
        date1 = 3000
    else:
        date1 = artwork1['Date']

    if artwork2['Date'] == "Unknown" or artwork2['Date'] == "" or len(artwork2['Date']) > 4:
        date2 = 3000
    else:
        date2 = artwork2['Date']        

    return int(date1) < int(date2) 
    
def compareIDs(authorname1, author):
    if (int(authorname1) == int(author['ConstituentID'])):
        return 0
    return -1 

# Funciones de ordenamiento

def sortArtistsBeginDate(list):
    sa.sort(list, compareBeginDates)

def sortArtworksDateAquired(list):
    ms.sort(list, compareDatesAquired)

def sortArtistByTechnique(list):
    ms.sort(list, compareTechnique)   

def sortNationalities(list):
    ms.sort(list, compareNationalities)     

def sortArtworksCost(list):
    ms.sort(list, compareCost) 

def sortArtworksDate(list):
    ms.sort(list, compareDate)        

#Auxiliar functions

def becomeDateAquiredToInt(Date):
    if Date == '':
        DateInt = 0
    else:
        year = str(Date[0]) + str(Date[1]) +str(Date[2]) + str(Date[3])
        month = str(Date[5]) + str(Date[6]) 
        day = str(Date[8]) + str(Date[9])    
         
        DateInt = int(year+month+day) 
        

    return DateInt
