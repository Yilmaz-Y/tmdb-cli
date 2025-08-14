import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(query):
    url = f"{BASE_URL}/search/movie"
    params =  {
        "api_key" : API_KEY,
        "query" : query
    }
    response = requests.get(url,params=params)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"API Error: {response.status_code}) - {response.text}")
    
def get_movies_by_type(movie_type):
    endpoint_map = {
        "playing" : "/movie/now_playing",
        "popular" : "/movie/popular",
        "top" : "/movie/top_rated",
        "upcoming" : "/movie/upcoming"
    }

    if movie_type not in endpoint_map:
        raise ValueError(f"Invalid type: {movie_type}")
    
    url = f"{BASE_URL}{endpoint_map[movie_type]}"
    params = {
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")