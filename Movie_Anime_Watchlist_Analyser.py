# Movie/Anime Watchlist Analyser
# Course: 2026CSAE100 - Computational Thinking and Programming
# Team: Suhana Khan, Akshat Rana, Jayant Kumar

import csv
import os

FILE_NAME = "watchlist.csv"
FIELDS = ["title", "content_type", "genre", "status", "rating"]

def load_watchlist():
    """Read saved titles from the CSV file."""
    watchlist = []
    if not os.path.exists(FILE_NAME):
        return watchlist

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if all(field in row for field in FIELDS):
                    try:
                        row["rating"] = float(row["rating"])
                        watchlist.append(row)
                    except ValueError:
                        continue
    except (OSError, csv.Error):
        print("Could not read the CSV file. Starting with an empty watchlist.")
    return watchlist


def save_watchlist(watchlist):
    """Save all titles to the CSV file."""
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            for item in watchlist:
                writer.writerow(item)
        return True
    except OSError:
        print("Error: the watchlist could not be saved.")
        return False


def show_titles(watchlist):
    if len(watchlist) == 0:
        print("Your watchlist is empty.")
        return

    print("\n--- YOUR WATCHLIST ---")
    for number, item in enumerate(watchlist, start=1):
        print(f"{number}. {item['title']} | {item['content_type']} | "
              f"{item['genre']} | {item['status']} | Rating: {item['rating']}")


def add_title(watchlist):
    title = input("Enter title: ").strip()
    if title == "":
        print("Title cannot be empty.")
        return

    for item in watchlist:
        if item["title"].lower() == title.lower():
            print("This title is already in your watchlist.")
            return

    content_type = input("Type (Movie/Anime): ").strip().title()
    if content_type not in ["Movie", "Anime"]:
        print("Please enter Movie or Anime.")
        return

    genre = input("Enter genre: ").strip().title()
    if genre == "":
        print("Genre cannot be empty.")
        return

    status = input("Status (Planned/Watching/Completed): ").strip().title()
    if status not in ["Planned", "Watching", "Completed"]:
        print("Invalid status.")
        return

    rating_text = input("Rating (0 to 10, enter 0 if not rated): ").strip()
    try:
        rating = float(rating_text)
        if rating < 0 or rating > 10:
            print("Rating must be between 0 and 10.")
            return
    except ValueError:
        print("Rating must be a number.")
        return

    watchlist.append({
        "title": title.title(),
        "content_type": content_type,
        "genre": genre,
        "status": status,
        "rating": rating
    })
    save_watchlist(watchlist)
    print("Title added successfully.")


def search_titles(watchlist):
    query = input("Enter title, genre or status to search: ").strip().lower()
    if query == "":
        print("Search cannot be empty.")
        return

    found = False
    for item in watchlist:
        if (query in item["title"].lower()
                or query in item["genre"].lower()
                or query == item["status"].lower()):
            print(item["title"], "|", item["genre"], "|",
                  item["status"], "| Rating:", item["rating"])
            found = True
    if not found:
        print("No matching title found.")


def update_title(watchlist):
    title = input("Enter the exact title to update: ").strip().lower()
    for item in watchlist:
        if item["title"].lower() == title:
            print("1. Update status")
            print("2. Update rating")
            choice = input("Choose: ").strip()

            if choice == "1":
                status = input("New status (Planned/Watching/Completed): ").strip().title()
                if status in ["Planned", "Watching", "Completed"]:
                    item["status"] = status
                    save_watchlist(watchlist)
                    print("Status updated.")
                else:
                    print("Invalid status.")
            elif choice == "2":
                try:
                    rating = float(input("New rating (0 to 10): "))
                    if 0 <= rating <= 10:
                        item["rating"] = rating
                        save_watchlist(watchlist)
                        print("Rating updated.")
                    else:
                        print("Rating must be between 0 and 10.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Invalid choice.")
            return
    print("Title not found.")


def delete_title(watchlist):
    title = input("Enter the exact title to delete: ").strip().lower()
    for item in watchlist:
        if item["title"].lower() == title:
            confirm = input("Delete this title? (yes/no): ").strip().lower()
            if confirm == "yes":
                watchlist.remove(item)
                save_watchlist(watchlist)
                print("Title deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Title not found.")


def analyse_watchlist(watchlist):
    if len(watchlist) == 0:
        print("No data available for analysis.")
        return

    total = len(watchlist)
    completed = 0
    rated_total = 0
    rating_sum = 0
    genre_counts = {}
    completed_genres = set()
    high_rated = []

    for item in watchlist:
        if item["status"] == "Completed":
            completed += 1
            completed_genres.add(item["genre"])

        if item["rating"] > 0:
            rated_total += 1
            rating_sum += item["rating"]
            if item["rating"] >= 8:
                high_rated.append(item["title"])

        genre = item["genre"]
        if genre not in genre_counts:
            genre_counts[genre] = 0
        genre_counts[genre] += 1

    print("\n--- WATCHLIST ANALYSIS ---")
    print("Total titles:", total)
    print("Completed titles:", completed)
    print("Planned/Watching titles:", total - completed)

    if rated_total > 0:
        print("Average personal rating:", round(rating_sum / rated_total, 2))
    else:
        print("Average personal rating: No ratings available")

    print("\nGenre-wise title count:")
    for genre, count in genre_counts.items():
        print(genre, ":", count)

    if len(high_rated) > 0:
        print("\nHighly rated titles (8 or above):", ", ".join(high_rated))
    else:
        print("\nNo highly rated titles yet.")

    print("Genres represented among completed titles:",
          ", ".join(sorted(completed_genres)) if completed_genres else "None")


def rank_titles(watchlist):
    rated_titles = []
    for item in watchlist:
        if item["rating"] > 0:
            rated_titles.append(item)

    if len(rated_titles) == 0:
        print("No rated titles available for ranking.")
        return

    ranked = sorted(rated_titles, key=lambda item: item["rating"], reverse=True)
    print("\n--- TOP RATED TITLES ---")
    for position, item in enumerate(ranked, start=1):
        print(position, item["title"], "-", item["rating"], "/ 10")


def recommend_titles(watchlist):
    genre_ratings = {}
    genre_counts = {}

    for item in watchlist:
        if item["status"] == "Completed" and item["rating"] > 0:
            genre = item["genre"]
            if genre not in genre_ratings:
                genre_ratings[genre] = 0
                genre_counts[genre] = 0
            genre_ratings[genre] += item["rating"]
            genre_counts[genre] += 1

    if len(genre_ratings) == 0:
        print("Complete and rate at least one title to get recommendations.")
        return

    favourite_genres = set()
    for genre in genre_ratings:
        average = genre_ratings[genre] / genre_counts[genre]
        if average >= 7:
            favourite_genres.add(genre)

    if len(favourite_genres) == 0:
        print("No favourite genre found yet. Rate a completed title 7 or above.")
        return

    recommendations = []
    for item in watchlist:
        if item["genre"] in favourite_genres and item["status"] != "Completed":
            recommendations.append(item)

    print("\nFavourite genres:", ", ".join(sorted(favourite_genres)))
    if len(recommendations) == 0:
        print("No unwatched titles from your favourite genres are in the list.")
    else:
        print("Suggested titles:")
        for item in recommendations:
            print("-", item["title"], "(", item["genre"], "/", item["status"], ")")


def main():
    watchlist = load_watchlist()
    while True:
        print("\n====== MOVIE/ANIME WATCHLIST ANALYSER ======")
        print("1. Add title")
        print("2. View watchlist")
        print("3. Search title")
        print("4. Update title")
        print("5. Delete title")
        print("6. Analyse watchlist")
        print("7. Rank highly rated titles")
        print("8. Get recommendations")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_title(watchlist)
        elif choice == "2":
            show_titles(watchlist)
        elif choice == "3":
            search_titles(watchlist)
        elif choice == "4":
            update_title(watchlist)
        elif choice == "5":
            delete_title(watchlist)
        elif choice == "6":
            analyse_watchlist(watchlist)
        elif choice == "7":
            rank_titles(watchlist)
        elif choice == "8":
            recommend_titles(watchlist)
        elif choice == "9":
            save_watchlist(watchlist)
            print("Watchlist saved. Goodbye!")
            break
        else:
            print("Invalid menu choice. Enter a number from 1 to 9.")


if __name__ == "__main__":
    main()