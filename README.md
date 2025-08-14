# TMDB CLI

This project is a Python-based Command Line Interface (CLI) application that uses [The Movie Database (TMDB)](https://www.themoviedb.org/) API to display movie, TV show, and person information directly from the terminal.  
It is based on the [roadmap.sh TMDB CLI Project](https://roadmap.sh/projects/tmdb-cli).

---

## Features

- Search for movies, TV shows, and people via TMDB API
- List popular movies
- Get detailed information about a specific movie
- View latest movie releases
- Show IMDb-like ratings
- Easy to use from the command line

---

## Requirements

- Python 3.8+
- TMDB API key ([How to Get an API Key](https://developer.themoviedb.org/docs/getting-started))

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tmdb-cli.git
   cd tmdb-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your TMDB API key to a `.env` file:
   ```env
   TMDB_API_KEY=your_api_key_here
   ```

---

## Usage

Run the following commands in your terminal:

- **List Popular Movies**
  ```bash
  python main.py popular
  ```

- **Search for a Movie**
  ```bash
  python main.py search "Inception"
  ```

- **Get Movie Details by ID**
  ```bash
  python main.py movie 27205
  ```

- **List Latest Movies**
  ```bash
  python main.py latest
  ```

---

## Example Output

```text
🎬 Title: Inception (2010)
   Rating: 8.3
   Overview: A thief who steals corporate secrets through dream-sharing technology...
```

---

## License

This project is licensed under the MIT License.
