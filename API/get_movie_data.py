import requests
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

# Function to get the list of movies
def get_movie(movie):
    # API URL for the TMDB (The movies database)
    TMDB_URL = "https://api.themoviedb.org/3/search/movie"
            
    # Making the request to TMDB
    response = requests.get(url=TMDB_URL, params={"api_key": os.getenv('api_key'), "query": movie})
    data = response.json()["results"] # Json data
    return data