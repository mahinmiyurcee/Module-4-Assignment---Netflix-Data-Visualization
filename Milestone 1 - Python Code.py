import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Data Preparation
# Assuming the CSV file is in your downloads folder
try:
    df = pd.read_csv('~/Downloads/Netflix_shows_movies.csv')
except FileNotFoundError:
    print("File not found. Please make sure the CSV file is in your Downloads folder.")
    exit()

# Print the first few rows and data info for debugging
print(df.head())
print(df.info())

# 2. Data Cleaning
# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Fill missing values (example: fill with 'Unknown' for categorical variables)
categorical_columns = ['director', 'cast', 'country', 'rating', 'listed_in']
for col in categorical_columns:
    df[col] = df[col].fillna('Unknown')

# For numerical columns, you might want to fill with median or mean
# First, ensure 'duration' is numeric
df['duration'] = pd.to_numeric(df['duration'].str.extract('(\d+)', expand=False), errors='coerce')
df['duration'].fillna(df['duration'].median(), inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Ensure 'release_year' is numeric
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# 3. Data Exploration
# Describe the data
print("\nDataset description:")
print(df.describe())

# 4. Data Visualization

# Most watched genres
plt.figure(figsize=(12, 6))
df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Most Watched Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_genres.png')
plt.close()

# Ratings distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('ratings_distribution.png')
plt.close()

# Additional visualization: Release year distribution
plt.figure(figsize=(12, 6))
df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('release_years_distribution.png')
plt.close()

print("Visualizations have been saved as PNG files.")