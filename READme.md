# Movie Data Preprocessing and Analysis

This project focuses on cleaning, preprocessing, exploratory data analysis (EDA), feature engineering, and visualization of a movie dataset (mymoviedb.csv). The goal is to handle missing data, extract meaningful features, identify patterns and outliers, and visualize insights from the data.

Project Structure:

mymoviedb-analysis/
│
├── data/
│   ├── mymoviedb.csv               # Original raw dataset
│   ├── mymoviedb_cleaned.csv       # Cleaned dataset after preprocessing
│
├── outputs/
│   ├── popularity_vs_vote_count.png
│   ├── genre_count_distribution.png
│   ├── vote_average_distribution.png
│   ├── correlation_heatmap.png
│   ├── movies_released_per_month.png
│   ├── genre_frequency.png
│
├── notebooks/
│   ├── exploratory_analysis.ipynb  # (Optional) Notebook for initial EDA and plotting
│
├── scripts/
│   ├── movie_data_analysis.py      # Main script for data cleaning and visualization
│
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore file

How to Run:

1. Clone the repository:
   git clone (https://github.com/adityagopal1807/moviedata_analytics)
   cd mymoviedb-analysis

2. Install dependencies:
   python -m venv venv
   source venv/bin/activate       # For Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. Run the analysis script:
   python scripts/movie_data_analysis.py

This will clean the data, perform feature engineering, handle outliers, and save visualizations in the outputs/ folder.

Features:
- Data cleaning and missing value handling
- Feature extraction (Year, Month, Genre count)
- Popularity normalization
- Outlier detection and removal (IQR method)
- Summary statistics and insights
- Visualizations showing trends and patterns

Dependencies:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

License:
MIT License


requirements

pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
seaborn==0.12.2
scikit-learn==1.2.2
