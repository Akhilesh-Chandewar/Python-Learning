import os
import json
from typing import List, TypedDict


class Movie(TypedDict):
    title: str
    year: str
    genre: str
    rating: float


FILE_NAME = "day_3_movies.json"


def load_movies() -> List[Movie]:
    """Load movies from JSON file or return empty list if file does not exist."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data: List[Movie] = json.load(f)
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_movies(movies: List[Movie]) -> None:
    """Save movies back to JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)


def add_movie(movies: List[Movie]) -> None:
    """Add a new movie with validation."""
    title = input("Enter movie title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return
    title_lower = title.lower()

    # Check if movie already exists
    if any(movie["title"].lower() == title_lower for movie in movies):
        print("❌ Movie already exists.")
        return

    year = input("Enter movie year: ").strip()
    if not year.isdigit() or not (1888 <= int(year) <= 2100):
        print("❌ Invalid year. Please enter a valid year (1888–2100).")
        return

    genre = input("Enter movie genre: ").strip()
    if not genre:
        print("❌ Genre cannot be empty.")
        return

    rating = input("Enter movie rating (0–10): ").strip()
    try:
        rating_value = float(rating)
        if not (0 <= rating_value <= 10):
            raise ValueError
    except ValueError:
        print("❌ Invalid rating. Please enter a number between 0 and 10.")
        return

    movie: Movie = {
        "title": title,
        "year": year,
        "genre": genre,
        "rating": rating_value,
    }
    movies.append(movie)
    save_movies(movies)
    print(f"✅ Movie '{title}' added successfully!")


def search_movie(movies: List[Movie]) -> None:
    """Search for a movie by title."""
    if not movies:
        print("📂 No movies in the database yet.")
        return

    query = input("Enter movie title to search: ").strip().lower()
    if not query:
        print("❌ Search query cannot be empty.")
        return

    found = [m for m in movies if query in m["title"].lower()]

    if not found:
        print("🔍 No matching movies found.")
        return

    print(f"\n🎬 Found {len(found)} movie(s):")
    for movie in found:
        print(
            f"- {movie['title']} ({movie['year']}) | "
            f"Genre: {movie['genre']} | Rating: {movie['rating']}"
        )



def main():
    movies = load_movies()

    while True:
        print("\n📽️ Movie Manager")
        print("1. Add Movie")
        print("2. List Movies")
        print("3. Search Movie")
        print("4. Save & Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_movie(movies)

        elif choice == "2":
            if not movies:
                print("📂 No movies in the database yet.")
            else:
                print("\n🎬 Movies:")
                for m in movies:
                    print(
                        f"- {m['title']} ({m['year']}) | "
                        f"Genre: {m['genre']} | Rating: {m['rating']}"
                    )

        elif choice == "3":
            search_movie(movies)

        elif choice == "4":
            save_movies(movies)
            print("💾 Movies saved. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
