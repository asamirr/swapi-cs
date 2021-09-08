import requests
from timing import timing

@timing
def getCharacterPlanetInfo(name):
    characterResponse = requests.get('https://swapi.dev/api/people/?search='+name).json()
    if(characterResponse['count'] == 0):
        return {'error': 'Not Found'}

    result = []

    for character in characterResponse['results']:
        query = {}

        
        query["character_name"] = character['name']
        query["gender"] = character['gender']
        
        planetUrl = character['homeworld']
        planetName = getPlanetInfoOnUrl(planetUrl)
        
        query["planet_name"] = planetName
        
        speciesUrl = character['species']
        species = getSpeciesInfo(speciesUrl)
        
        query['species'] = species['name']
        query['lifespan'] = species['lifespan']

        moviesUrl = character['films']
        moviesInfo = getMoviesInfo(moviesUrl)
        
        query["list_of_films"] = moviesInfo

        result.append(query)

    return result

@timing
def getPlanetInfoOnUrl(url):
    planetResponse = requests.get(url).json()
    planet = planetResponse['name']

    return planet

@timing
def getMoviesInfo(url):
    filmsResponse = url
    films = []

    for film in filmsResponse:
        filmURL = requests.get(film).json()
        films.append(filmURL['title'])
    return films

@timing
def getSpeciesInfo(url):
    speciesResponse = url
    species_names = ""
    species_lifespan = ""
    for species_inst in speciesResponse:
        speciesUrl = requests.get(species_inst).json()
        species_names = speciesUrl['name']
        species_lifespan = speciesUrl['average_lifespan']

    return {'name': species_names, 'lifespan': species_lifespan}