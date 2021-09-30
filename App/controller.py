

from DISClib.ADT.list import iterator
from DISClib.ADT import list as lt
import config as cf
import model
import csv


# Inicialización del Catálogo de libros
def initCatalog():
    
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    
    loadArtists(catalog)
    loadArtworks(catalog)
    loadArtistsNames(catalog)
    loadMedium(catalog)



def loadArtists(catalog):
    
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    tagsfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def loadMedium (catalog):
 
    for artwork in lt.iterator(catalog['artworks']):
        model.addMedium(catalog , artwork['Medium']  )
    
    
def loadArtistsNames(catalog):
    model.loadArtistsNames(catalog)        
  
        



# Funciones de ordenamiento

def sortArtistsBeginDate(catalog):
    model.sortArtistsBeginDate(catalog)

def sortArtworksDateAquired(catalog):
    model.sortArtworksDateAquired(catalog)  

def sortArtworksCost(list):
    model.sortArtworksCost(list)

def sortArtworksDate(list):
    model.sortArtworksDate(list)          


# Funciones de consulta sobre el catálogo

def artistsByDates(catalog,date1,date2):
    return model.artistsByDates(catalog,date1,date2)

def artworksByDates(catalog,date1,date2):
    return model.artworksByDates(catalog,date1,date2)

def artworkArtistByTechnique(catalog,artist):
    return model.artworkArtistByTechnique(catalog,artist)

def artworksByNationality(catalog):
    return model.artworksByNacionality(catalog)    

def objectsByNacionality(catalog,nationality):
    return model.objectsOfNacionality(catalog,nationality)  

def transportCostByDepartment(catalog,department):
    return model.transportCostByDepartment(catalog,department)  

def newExposition(catalog,date1,date2,area):
    return model.newExposition(catalog,date1,date2,area)        