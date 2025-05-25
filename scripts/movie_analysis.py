# -------------------------------
# Movie Data Preprocessing & EDA
# -------------------------------

# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import os

# Configure visual settings
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Create output folder for visualizations
os.makedirs('visuals_output', exist_ok=True)

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv('data/mymoviedb.csv', lineterminator='\n')
print("✅ Dataset Loaded Successfully\n")
print(df.head())

# -------------------------------
# 2. Data Cleaning
# -------------------------------

# Check for missing values
print("\n📌 Missing Values Check:")
print(df.isnull().sum())

# Convert 'Release_Date' to datetime
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')

# Fill missing text fields with placeholders
df['Overview'] = df['Overview'].fillna('Not Available')
df['Poster_Url'] = df['Poster_Url'].fillna('Not Available')

# Drop rows where Release_Date could not be parsed
df.dropna(subset=['Release_Date'], inplace=True)

# -------------------------------
# 3. Feature Engineering
# -------------------------------

# Extract year and month from release date
df['Year'] = df['Release_Date'].dt.year
df['Month'] = df['Release_Date'].dt.month

# Calculate number of genres for each movie
df['Genre_Count'] = df['Genre'].apply(lambda x: len(str(x).split(',')))

# Normalize popularity using MinMaxScaler
scaler = MinMaxScaler()
df['Popularity_Norm'] = scaler.fit_transform(df[['Popularity']])

# -------------------------------
# 4. Data Integrity & Consistency
# -------------------------------

# Remove duplicate rows if any
duplicates = df.duplicated().sum()
print(f"\n🧹 Duplicate Rows Removed: {duplicates}")
df.drop_duplicates(inplace=True)

# Fix data types
df['Vote_Count'] = df['Vote_Count'].astype(int)
df['Vote_Average'] = df['Vote_Average'].astype(float)

# -------------------------------
# 5. Summary Statistics & Insights
# -------------------------------

print("\n📊 Summary Statistics:\n")
print(df.describe())

# Display the most voted movie
most_voted = df[df['Vote_Count'] == df['Vote_Count'].max()]
print("\n🏆 Most Voted Movie:")
print(most_voted[['Title', 'Vote_Count', 'Vote_Average']])

# -------------------------------
# 6. Outlier Handling
# -------------------------------

# Remove outliers in 'Popularity' using IQR method
Q1 = df['Popularity'].quantile(0.25)
Q3 = df['Popularity'].quantile(0.75)
IQR = Q3 - Q1
df_no_outliers = df[~((df['Popularity'] < (Q1 - 1.5 * IQR)) | (df['Popularity'] > (Q3 + 1.5 * IQR)))]

outliers_removed = df.shape[0] - df_no_outliers.shape[0]
print(f"\n⚠️ Outliers Removed (Popularity): {outliers_removed}")

# -------------------------------
# 7. Data Visualization
# -------------------------------

# Scatter plot: Popularity vs Vote Count
plt.figure()
sns.scatterplot(data=df, x='Popularity', y='Vote_Count', hue='Title', legend=False)
plt.title("Popularity vs Vote Count")
plt.xlabel("Popularity")
plt.ylabel("Vote Count")
plt.tight_layout()
plt.savefig('visuals_output/popularity_vs_votes.png')
plt.close()

# Bar plot: Genre Count Distribution
plt.figure()
sns.countplot(data=df, x='Genre_Count')
plt.title("Number of Genres per Movie")
plt.xlabel("Genre Count")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig('visuals_output/genre_count_distribution.png')
plt.close()

# Histogram: Vote Average Distribution
plt.figure()
sns.histplot(df['Vote_Average'], bins=10, kde=True)
plt.title("Vote Average Distribution")
plt.xlabel("Vote Average")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig('visuals_output/vote_average_distribution.png')
plt.close()

# Correlation Heatmap
plt.figure()
sns.heatmap(df[['Popularity', 'Vote_Count', 'Vote_Average', 'Genre_Count']].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig('visuals_output/correlation_heatmap.png')
plt.close()

# Movie releases by Month
plt.figure()
sns.countplot(data=df, x='Month', order=sorted(df['Month'].dropna().unique()))
plt.title("Movie Releases by Month")
plt.xlabel("Month")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig('visuals_output/monthly_release.png')
plt.close()

print("\n✅ Visualizations Saved in 'visuals_output/' Folder")

# -------------------------------
# 8. Save Cleaned Dataset
# -------------------------------
df.to_csv("data/mymoviedb_cleaned.csv", index=False)
print("📁 Cleaned dataset saved to 'data/mymoviedb_cleaned.csv'")
