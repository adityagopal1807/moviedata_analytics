# movie_data_bar_charts.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_outputs_dir():
    """Create outputs folder if it doesn't exist."""
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

def preprocess_data(file_path):
    """Load and preprocess movie dataset."""
    df = pd.read_csv(file_path)

    # Convert release_date to datetime and extract year
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['release_year'] = df['release_date'].dt.year

    # Drop rows with missing release_year or genres
    df = df.dropna(subset=['release_year', 'genres'])

    # Explode genres into separate rows
    df['genres'] = df['genres'].str.split('|')
    df_exploded = df.explode('genres').reset_index(drop=True)

    return df_exploded

def plot_genre_count(df):
    """Plot number of movies per genre."""
    genre_counts = df['genres'].value_counts()

    plt.figure(figsize=(12,6))
    sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
    plt.title('Number of Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/genre_count_distribution.png')
    plt.show()

def plot_avg_vote_by_genre(df):
    """Plot average vote by genre."""
    avg_vote_genre = df.groupby('genres')['vote_average'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    sns.barplot(x=avg_vote_genre.index, y=avg_vote_genre.values, palette='magma')
    plt.title('Average Movie Vote by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Vote')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/avg_vote_by_genre.png')
    plt.show()

def plot_movies_released_per_year(df):
    """Plot number of movies released per year."""
    movies_per_year = df['release_year'].value_counts().sort_index()

    plt.figure(figsize=(14,6))
    sns.barplot(x=movies_per_year.index, y=movies_per_year.values, palette='cubehelix')
    plt.title('Number of Movies Released Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/movies_released_per_year.png')
    plt.show()

def main():
    create_outputs_dir()
    data_file = 'data/mymoviedb.csv'  # Change path if needed
    df = preprocess_data(data_file)

    plot_genre_count(df)
    plot_avg_vote_by_genre(df)
    plot_movies_released_per_year(df)

if __name__ == "__main__":
    main()
