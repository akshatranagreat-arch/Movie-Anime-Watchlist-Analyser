# Movie/Anime Watchlist Analyser

A menu-driven Python console application developed for **Computational Thinking and Programming (2026CSAE100)** at Bennett University.

The program helps users maintain a combined movie and anime watchlist, track viewing progress and personal ratings, analyse their list, rank rated titles, and receive simple rule-based recommendations.

## Team

| Name | Enrollment number |
|---|---|
| Suhana Khan | S26CSEU0170 |
| Akshat Rana | S26CSEU0138 |
| Jayant Kumar | S26CSEU0166 |

## Features

1. Add a movie or anime title with its genre, status, and rating.
2. View all saved entries.
3. Search by title, genre, or status.
4. Update a title's status or rating.
5. Delete an entry with confirmation.
6. Analyse totals, completed titles, average personal rating, genre counts, highly rated titles, and genres represented among completed titles.
7. Rank rated titles from highest to lowest rating.
8. Recommend non-completed titles from genres whose completed-title average rating is at least 7.
9. Save the watchlist to CSV and reload it when the program starts.

## Requirements

- Python 3
- No third-party packages required.

## Run

Keep `Movie_Anime_Watchlist_Analyser.py` and `watchlist.csv` in the same directory. Run:

```bash
python Movie_Anime_Watchlist_Analyser.py
```

On Windows, `py Movie_Anime_Watchlist_Analyser.py` may also be used.

## CSV data

The CSV fields are `title`, `content_type`, `genre`, `status`, and `rating`. A rating of 0 represents an unrated title. The included records are illustrative sample data for demonstration; replace them with your own entries when using the application.

## Python concepts

Variables and data types, conditionals, loops, lists, dictionaries, sets, functions, string methods, sorting with `sorted()`, CSV file handling, and basic exception handling.

## Recommendation logic

The program calculates the average of non-zero ratings for completed titles in each genre. Genres with an average of at least 7 are treated as favourite genres. It then suggests titles in those genres that are not marked Completed. This is a rule-based method, not machine learning.

## Acknowledgements

- [Python documentation](https://docs.python.org/3/)
- [Python CSV module documentation](https://docs.python.org/3/library/csv.html)
