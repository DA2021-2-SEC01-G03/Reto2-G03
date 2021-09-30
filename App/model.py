
from DISClib.DataStructures.arraylist import isPresent
import config as cf
import operator
from DISClib.ADT import map 
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

# Construccion de modelos

def newCatalog(): 
   
    catalog = {'artists': None,
               'artworks': None,
               }

    catalog['artists'] = lt.newList('ARRAY_LIST',cmpfunction= compareIDs)
    catalog['artworks'] = lt.newList('ARRAY_LIST')
    catalog['medium'] = map.newMap()
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):

    lt.addLast(catalog['artists'], artist)
    
     

def addArtwork(catalog, artwork):

    lt.addLast(catalog['artworks'], artwork)
    constituents = artwork['ConstituentID'][1:][:-1].split(",")
    artwork['Constituents'] = constituents
    if artwork['Height (cm)'] != '' and artwork['Width (cm)'] != '' and artwork['Depth (cm)'] == '' and artwork['Length (cm)'] == '':
       artwork['Area'] = (float(artwork['Height (cm)']) * float(artwork['Width (cm)']))/100   
    else:
        artwork['Area'] = 0 

def addMedium(catalog, medium):
    map.put(catalog['medium'] , map.size(catalog['medium']) + 1, medium )


def obras_mas_antiguas(catalog, obras, medio):
    


             

def loadArtistsNames(catalog):
    for artworks in lt.iterator(catalog['artworks']):
       artworks['ArtistsNames'] = []
       artworks['Nationality'] = []
       constituents = artworks['Constituents']  
       i = 0
       tam = len(constituents)
       while i < tam:
           pos = lt.isPresent(catalog['artists'],constituents[i])
           artist = lt.getElement(catalog['artists'],pos)
           artworks['ArtistsNames'].append(artist['DisplayName'])
           artworks['Nationality'].append(artist['Nationality'])
           i += 1
           


                
    



# Funciones para creacion de datos

# Funciones de consulta

def artistsByDates(catalog, date1:int, date2:int):

    list = lt.newList()
    artists = catalog['artists']
    i = 1
    tam = lt.size(artists)
    count = 1
    while i < tam:
      dict = lt.getElement(artists, i)
      if (int(dict['BeginDate']) >= date1) and (int(dict['BeginDate']) <= date2):
          lt.addLast(list, dict)
          count += 1
      i += 1
    return (list,count)



def artworksByDates(catalog, date1, date2):
    list = lt.newList()
    artworks = catalog['artworks']
    i = 1
    tam = lt.size(artworks)
    count = 0
    while i < tam:
      dict = lt.getElement(artworks, i) 
      DateInt = becomeDateAquiredToInt(dict['DateAcquired'])
      if DateInt > date1 and DateInt < date2:
         lt.addLast(list, dict)
         count += 1   
      i += 1           

    return (list,count)               



def artworkArtistByTechnique(catalog,artist):
    artistHistogramTechnique = {}
    idArtist = ""
    countPieces = 0
    countTechnique = 0

    for artist1 in lt.iterator(catalog['artists']):
            if artist1['DisplayName'] == artist:
                idArtist = artist1['ConstituentID']
                break
    for artwork in lt.iterator(catalog['artworks']):
            if artist in artwork['ArtistsNames']:              
                technique = artwork['Medium']
                artistHistogramTechnique[technique] = 0
                countTechnique += 1
    for artwork in lt.iterator(catalog['artworks']):
            if artist in artwork['ArtistsNames']:               
                technique = artwork['Medium']
                artistHistogramTechnique[technique] += 1 
                countPieces += 1

    sortedDict = sorted(artistHistogramTechnique.items(), key=operator.itemgetter(1))            
          
    return sortedDict,idArtist,countPieces,countTechnique



def artworksByNacionality(catalog):
    artworks = catalog['artworks']
    nationalitysHistogram = {}
    for artwork in lt.iterator(artworks):
        i = 0
        tam = len(artwork['Nationality'])
        while i < tam:
            nationality = artwork['Nationality'][i]
            nationalitysHistogram[nationality] = 0
            i += 1
    for artwork in lt.iterator(artworks):
        tam2 = len(artwork['Nationality'])        
        j = 0    
        while j < tam2:
            nationality = artwork['Nationality'][j]
            nationalitysHistogram[nationality] += 1 
            j += 1    
            
    sortedDict = sorted(nationalitysHistogram.items(), key=operator.itemgetter(1))        

    return sortedDict



def objectsOfNacionality(catalog,Nationality):
    artworks = catalog['artworks']
    listNationality = lt.newList()
    for artwork in lt.iterator(artworks):
        if Nationality in artwork['Nationality']:
            lt.addLast(listNationality, artwork)

    return listNationality        



def transportCostByDepartment(catalog,department):
    artworks = catalog['artworks']
    listArtworks = lt.newList()
    costsSum = 0
    weightsSum = 0
    for artwork in lt.iterator(artworks):
        if artwork['Department'] == department:
           finalCost = 0

           if artwork['Weight (kg)'] != "":
            weight = float(artwork['Weight (kg)'])
            costWeight = 72/weight
           else:
            costWeight = 0  
            weight = 0

           if artwork['Height (cm)'] != "":
            height = float(artwork['Height (cm)']) 
           else: 
            height = 0

           if artwork['Width (cm)'] != "":
            width = float(artwork['Width (cm)'])     
           else:
            width = 0

           if artwork['Depth (cm)']: 
            depth = float(artwork['Depth (cm)'])
           else: 
            depth = 0


           costMettersSquared = 0
           costMettersCubed = 0
           if height != 0 and width != 0 and depth != 0:
              costMettersCubed = 72 / ((width*height*depth)/100)
           if height != 0 and width != 0:   
              costMettersSquared = 72 / ((width*height)/100)

           if costWeight == 0 and costMettersCubed == 0 and costMettersSquared == 0:
              finalCost = 42
           elif costWeight > costMettersCubed and costWeight > costMettersSquared:
              finalCost = costWeight
           elif costMettersCubed > costWeight and costMettersCubed > costMettersSquared:
              finalCost = costMettersCubed
           elif costMettersSquared > costWeight and costMettersSquared > costMettersCubed:
               finalCost = costMettersSquared
               artwork['Area'] = (width*height)/100

           artwork['cost'] = finalCost         
           costsSum += finalCost
           weightsSum += weight

           lt.addLast(listArtworks, artwork)    

    return ((listArtworks),costsSum,weightsSum)

def newExposition(catalog,date1,date2,area):
    artworks = catalog['artworks']
    Exposition = lt.newList()
    for artwork in lt.iterator(artworks):
        if artwork['Date'] != "" and len(artwork['Date']) == 4 and artwork['Date'] != "n.d."  and artwork['Area'] > 0 :
            if int(artwork['Date']) >= date1 and int(artwork['Date']) <= date2:
                lt.addLast(Exposition,artwork)

    return Exposition

    

# Funciones utilizadas para comparar elementos dentro de una lista

def compareBeginDates(artist1, artist2):
    return int(artist1['BeginDate']) < int(artist2['BeginDate'])

def compareDatesAquired(artwork1, artwork2):
    date1 = artwork1['DateAcquired']
    date2 = artwork2['DateAcquired']

    intDate1 = becomeDateAquiredToInt(date1)
    intDate2 = becomeDateAquiredToInt(date2)

    return intDate1 < intDate2

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

def sortArtistsBeginDate(catalog):
    sa.sort(catalog['artists'], compareBeginDates)

def sortArtworksDateAquired(catalog):
    ms.sort(catalog['artworks'], compareDatesAquired)

def sortArtworksCost(list):
    ms.sort(list,compareCost) 

def sortArtworksDate(list):
    ms.sort(list,compareDate)        

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
