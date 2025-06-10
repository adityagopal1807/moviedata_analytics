# Movie Data Preprocessing and Analysis

## Project Overview

This project presents a comprehensive analysis pipeline for a movie dataset (`mymoviedb.csv`), focusing on data cleaning, preprocessing, exploratory data analysis (EDA), feature engineering, and visualization. The goal is to transform raw, messy data into actionable insights by handling missing values, detecting outliers, extracting meaningful features, and visually communicating trends and patterns in the film industry.

## Objectives

- Clean and preprocess the raw dataset to ensure quality and consistency.
- Handle missing data strategically to preserve dataset integrity.
- Engineer new features such as release year, month, and genre counts to enrich analysis.
- Detect and remove outliers using robust statistical methods (IQR).
- Normalize popularity metrics to allow fair comparison across movies.
- Perform detailed exploratory data analysis to uncover hidden trends.
- Generate clear, insightful, and aesthetically pleasing visualizations.
- Facilitate understanding of the dataset through interactive and annotated charts (where applicable).
- Document the entire process for reproducibility and further extension.

## Dataset Description

The dataset contains **[insert total number of records]** movies with key attributes including:

- **Title:** Movie title  
- **Release Date:** Date of release  
- **Genres:** One or multiple genre labels  
- **Popularity:** A numeric score indicating popularity  
- **Vote Count:** Number of user votes  
- **Vote Average:** Average rating  
- **Other Metadata:** Additional features as available  

The data is sourced from **[source, e.g., TMDB API or Kaggle]** and requires preprocessing to handle missing or inconsistent values.

## Project Structure

mymoviedb-analysis/
│
├── data/
│ ├── mymoviedb.csv # Raw dataset
│ ├── mymoviedb_cleaned.csv # Cleaned and preprocessed data
│
├── outputs/
│ ├── popularity_vs_vote_count.png
│ ├── genre_count_distribution.png
│ ├── vote_average_distribution.png
│ ├── correlation_heatmap.png
│ ├── movies_released_per_month.png
│ ├── genre_frequency.png
│
├── notebooks/
│ ├── exploratory_analysis.ipynb # Jupyter notebook for exploratory analysis and visualization experiments
│
├── scripts/
│ ├── movie_data_analysis.py # Main script for preprocessing, feature engineering, outlier removal, and visualization
│
├── README.md # This documentation file
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore file

markdown


## Visualizations & Insights

- **Popularity vs Vote Count (Scatter Plot):** Shows how vote counts correlate with popularity scores, revealing outliers and distribution clusters.
- **Genre Count Distribution (Bar Chart):** Visualizes the frequency of different movie genres, highlighting dominant categories.
- **Vote Average Distribution (Histogram):** Displays rating trends, indicating viewer preferences.
- **Correlation Heatmap:** Highlights relationships between numerical variables for multivariate insight.
- **Movies Released Per Month (Line Chart):** Unveils seasonal trends in movie releases.
- **Genre Frequency Over Time:** Tracks changes in genre popularity across years.

Each chart includes clear axis labels, legends, and color schemes to enhance readability. Key findings and outliers are annotated to facilitate storytelling.

## How to Use

### Prerequisites

- Python 3.8 or higher
- Recommended: virtual environment to isolate dependencies

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/adityagopal1807/moviedata_analytics.git
   cd mymoviedb-analysis
Create and activate a virtual environment:

Linux/macOS:

bash

python -m venv venv
source venv/bin/activate
Windows:

bash

python -m venv venv
venv\Scripts\activate
Install dependencies:

bash

pip install -r requirements.txt
Run the analysis script:

bash
python scripts/movie_data_analysis.py
This script cleans and preprocesses the data, performs feature engineering, removes outliers, and generates all visualizations saved in the outputs/ directory.

Exploring Visualizations
Open any .png files inside the outputs/ folder using your preferred image viewer. The notebooks/exploratory_analysis.ipynb provides interactive exploration and additional insights.

Dependencies
The project relies on the following libraries (specified in requirements.txt):

pandas==1.5.3

numpy==1.24.3

matplotlib==3.7.1

seaborn==0.12.2

scikit-learn==1.2.2

Contributing
Contributions and improvements are welcome! Feel free to fork the repo, open issues, or submit pull requests to enhance analysis, add new visualizations, or improve documentation.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Created by Aditya Gopal
GitHub: https://github.com/adityagopal1807

Thank you for reviewing my project! I hope these visualizations and analyses provide meaningful insights into movie trends and viewer behavior.
