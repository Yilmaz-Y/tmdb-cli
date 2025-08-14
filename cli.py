import argparse

from tmdb import search_movie, get_movies_by_type

def main():
    parser = argparse.ArgumentParser(description="TMDB CLI - Movie Search")
    
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--query",  help="Search with movie name")
    group.add_argument("--type", choices=["playing", "popular", "top", "upcoming"], help="List with type of movie")

    args = parser.parse_args()

    try:
        if args.query:
            results = search_movie(args.query)
        else:
            results = get_movies_by_type(args.type)

        if not results:
            print("Nothing found.")
            return
        
        for idx, movie in enumerate(results[:5], 1):
            title = movie.get("title") or movie.get("name")
            year = movie.get("release_date", "No year")[:4]
            overview = movie.get("overview", "No description")[:200]

            print(f"{idx}. {title} ({year})")
            print(f"        {overview}...\n")
    except Exception as e:
        print(f"Error: {e}")