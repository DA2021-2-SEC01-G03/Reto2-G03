
from operator import ne
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map
assert cf

def initCatalog():

    return controller.initCatalog()


def loadData(catalog):
    
    controller.loadData(catalog)


# Artists ByDates


def artistsByDates():
    
    list = controller.artistsByDates(catalog,date01,date02)[0]
    count = controller.artistsByDates(catalog,date01,date02)[1]
    controller.sortArtistsBeginDate(list)

    sizeList = lt.size(list)
 
    if sizeList:
      first3 = lt.subList(list,1,3)
      last3 = lt.subList(list,sizeList-3,3) 
      print("There are " + str(count) + " artists born between " + str(date01) + " and " + str(date02))
      print("")
      print("The first and last 3 artists in the range are...")  
      for artist in lt.iterator(first3):
        
             print('Name: ' + artist['DisplayName'] + '  Begin date: ' +
                  artist['BeginDate'] + ' End date: ' + artist['EndDate'] +
                  ' Nacionality: ' + artist['Nationality'] + ' Gender: ' + artist['Gender'])

      print("")            

      for artist in lt.iterator(last3):
        
             print('Name: ' + artist['DisplayName'] + '  Begin date: ' +
                  artist['BeginDate'] + ' End date: ' + artist['EndDate'] +
                  ' Nacionality: ' + artist['Nationality'] + ' Gender: ' + artist['Gender'])  
      
                  
    else:
        print("No se encontraron artistas")                       
           
#New Function

def artworksByDateAquired():
    list = controller.artworksByDates(catalog,date01,date02)[0]
    count = controller.artworksByDates(catalog,date01,date02)[1]
    controller.sortArtworksDateAquired(list)
    
    sizeList = lt.size(list)
 
    if sizeList:
      first3 = lt.subList(list,1,3)
      last3 = lt.subList(list,sizeList-2,3) 
      print("The MoMA acquired " + str(count) + " unique pieces between " + str(date01) + " and " + str(date02))
      print("")
      print("The first and last 3 artworks in the range are...")  
      print("")
      for artwork in lt.iterator(first3):
        
             print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
                  artwork['Title'] + ', ArtistsNames: ' + str(artwork['ArtistsNames']) +
                  ', Medium: ' + artwork['Medium'] + ', Dimensions: ' + artwork['Dimensions']
                  + ', Date: ' + artwork['Date'] + ', DateAcquired: ' + artwork['DateAcquired'] +
                  ', URL: ' + artwork['URL'])
      print("")            

      for artwork in lt.iterator(last3):
        
             print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
                  artwork['Title'] + ', ArtistsNames: ' + str(artwork['ArtistsNames']) +
                  ', Medium: ' + artwork['Medium'] + ', Dimensions: ' + artwork['Dimensions']
                  + ', Date: ' + artwork['Date'] + ', DateAcquired: ' + artwork['DateAcquired'] +
                  ', URL: ' + artwork['URL'])  
      
                  
    else:
        print("No se encontraron artistas") 

#New Function

def artworkArtistByTechnique():
    list = controller.artworkArtistByTechnique(catalog,artist)[0]
    idArtist = controller.artworkArtistByTechnique(catalog,artist)[1]
    countPieces = controller.artworkArtistByTechnique(catalog,artist)[2]
    countTechnique = controller.artworkArtistByTechnique(catalog,artist)[3]


    print(artist + " with MoMA ID " + idArtist + " has " + str(countPieces) + " pieces in her/his name at the museum.")
    print("There are " + str(countTechnique) + " diferent mediums/techniques in her/his work")
    print("")
    

    if countTechnique > 0:
     print("Her/his top 5 medium/technique are...")
     controller.sortArtistByTechnique(list)
     if lt.size(list) >= 5:
       first5 = lt.subList(list, 1, 5)
       for value in lt.iterator(first5):
           print( 'MediumName: ' + str(value['technique']) + ', count: ' + str(value['Number of artworks']) )
    
     else:
       for value in lt.iterator(list):
           print( 'MediumName: ' + str(value['technique']) + ', count: ' + str(value['Number of artworks']) )
      
     mostUsed = lt.firstElement(list)   

     techniqueBucket = map.get(catalog['Medium'], mostUsed['technique'])['value']
     sample = lt.newList('ARRAY_LIST')
     count = 0
     for artwork in lt.iterator(techniqueBucket):
         if count >= 3:
             break
         if artist in artwork['ArtistsNames']:
            lt.addLast(sample, artwork) 
            count += 1

    print("")
    print("Her/his most used medium/technique is " + str(mostUsed['technique']) + " with " + str(mostUsed['Number of artworks']) + " pieces")
    print("A sample of 3 " + str(mostUsed['technique']) + " form the collection are...")
    print("")
    for artwork in lt.iterator(sample):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] + ', Department: ' 
             + artwork['Department'] +  ', Classification: ' + artwork['Classification'] + 
             ', URL: ' + artwork['URL'])





#New Function
def byNationality():

    listNationalities = controller.artworksByNationality(catalog)
    controller.sortNationalities(listNationalities)
    top10 = lt.subList(listNationalities, 1, 10)
    topNationality = lt.firstElement(listNationalities)
    print("The TOP 10 countries in the MoMA are...")
    for nationality in lt.iterator(top10):
        print( 'Nationality: ' + str(nationality['Nationality']) + ', Artworks: ' + str(nationality['Count']) )

    print("The top Nationality in the museum is " + str(topNationality['Nationality']) + " with " + str(topNationality['Count']) + " unique pieces" )
    
    print("The first and last 3 objects in the " + str(topNationality['Nationality']) + " artwork list are...")
    print("")
    
    artworksNationality = controller.artworksOfNacionality(catalog, topNationality['Nationality'])
    sizeList = lt.size(artworksNationality)

    first3 = lt.subList(artworksNationality,sizeList-2,3)
    last3 = lt.subList(artworksNationality,1,3)

    for artwork in lt.iterator(first3):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] + ', Department: ' 
             + artwork['Department'] +  ', Classification: ' + artwork['Classification'] + 
             ', URL: ' + artwork['URL'])

    print("")

    for artwork in lt.iterator(last3):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] + ', Department: ' 
             + artwork['Department'] +  ', Classification: ' + artwork['Classification'] + 
             ', URL: ' + artwork['URL'])


def transportCostByDepartment():
    
    list = controller.transportCostByDepartment(catalog,department)[0]
    totalCost = controller.transportCostByDepartment(catalog,department)[1]
    totalWeight = controller.transportCostByDepartment(catalog,department)[2]
    totalArtworks = lt.size(list)
    print("The MoMA is going to transport " + str(totalArtworks) + " artifacts from the " + str(department) + " MoMA's department")
    print("REMEMBER!, NOT all MoMA´s data is complete!!!... These are estimates")
    print("Estimated cargo weight (kg): " + str(round(totalWeight,2)))
    print("Estimated cargo cost (USD): " + str(round(totalCost,2)))

     
    controller.sortArtworksCost(list) 
    top5Expensive = lt.subList(list,lt.size(list)-5,5)

    print("")
    print("The most 5 expensive items to transport are...")
    
    for artwork in lt.iterator(top5Expensive):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] + ', Department: ' 
             + artwork['Department'] +  ', Classification: ' + artwork['Classification'] + 
              ', TransCost (USD): ' + str(artwork['cost']) + ', URL: ' +  artwork['URL'])

    print("")

    controller.sortArtworksDate(list)
    top5Oldest = lt.subList(list,1,5)
    
   
    print("The top 5 oldest items to transport are...")   

    for artwork in lt.iterator(top5Oldest):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', ArtistsNames: ' + str(artwork['ArtistsNames']) +
              ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] +  ', Classification: ' + artwork['Classification'] + 
               ', TransCost (USD): ' + str(artwork['cost']) + ', URL: ' + artwork['URL']) 
        

    
#Menu


def printMenu():
    print("Bienvenido")
    print("1- Load artists and artworks information")
    print("2- list chronologically artists born in a range of years") 
    print("3- list chronologically artworks by date acquired")
    print("4- Artworks of an artist by technique") 
    print("5- Nationalitys with most artworks")
    print("6- Artworks cost by department")
    print("0- Salir")

catalog = None

while True:
    printMenu()
    inputs = input('Select an option to continue\n')
    if int(inputs) == 1:
        print("Loading files information ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Arstists loaded: ' + str(lt.size(catalog['artists'])))
        print('Artworks loaded: ' + str(lt.size(catalog['artworks'])))
        


    elif int(inputs) == 2:
        date01 = int(input('First year (YYYY) '))
        date02 = int(input('Last year (YYYY) '))
        artistsByDates()

    elif int(inputs) == 3:
        date01 = int(input('First Date (AAAAMMDD) '))
        date02 = int(input('Last Date  (AAAAMMDD) '))
        artworksByDateAquired()     

    elif int(inputs) == 4:
        artist = input("Enter the artist name ")
        artworkArtistByTechnique()


    elif int(inputs) == 5:
        byNationality()
    

    elif int(inputs) == 6:
        department = input("Enter department ")
        transportCostByDepartment()

    else:
        sys.exit(0)
        
