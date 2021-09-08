# Star Wars API

## To start the container 

After cloning the project, first build the image 

`docker build -t swapi-docker:v1 .`

Then start the container 

`docker run -t -i -p 8000:5000 swapi-docker:v1`

Go to the browser and visit `http://localhost:8000/character/<name>/` and type any name.

For example, when you visit `http://localhost:8000/character/R2/` you should expect the following response:

`[
  {
    "character_name": "R2-D2", 
    "gender": "n/a", 
    "lifespan": "indefinite", 
    "list_of_films": [
      "A New Hope", 
      "The Empire Strikes Back", 
      "Return of the Jedi", 
      "The Phantom Menace", 
      "Attack of the Clones", 
      "Revenge of the Sith"
    ], 
    "planet_name": "Naboo", 
    "species": "Droid"
  }
]`

## To run the app without Docker

Just `cd swapi-cs` then `python main.py`

Paste `http://192.168.1.39:5000/character/<name>/` or whatever URL you in the terminal 
and start testing with names!






