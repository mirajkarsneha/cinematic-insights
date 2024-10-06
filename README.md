# 🎥 Cinematic Insights 🍿

## 🎟️ Description
Based on a combination of an OMDB dataframe and OMDB API we are trying to identify the most commercially successful genre and optimal runtime for a new movie to be released in the near future, given current audience preferences and market trends. After the elaboration of th business question we came up with the 3 following hypothesis, that will be accepted or rejected, after our analysis:

### 🌟  H1: Genre Popularity
'Genres with higher average ratings and vote counts in the past 10 years will likely be more successful in terms of box office earnings’

### 👥  H2: Audience Trends
'There is a correlation between a movie's financial success and the popularity of its featured actors'

### 🎞️  H3: Runtime Preference
‘Movies with a runtime between 120 and 150 minutes tend to perform better commercially'

## 📺 Prerequisites
- Python Project
- OMDB API link- https://www.omdbapi.com/<br>
- Dataset link- https://www.kaggle.com/datasets/amanbarthwal/imdb-movies-data
- Git Hub link- https://github.com/mirajkarsneha/cinematic-insights
- Trello link- https://trello.com/b/Hj5kYts9/project-cinematic-insights
- Presentation link - https://docs.google.com/presentation/d/1WdLSx_zLLusT_XJDlD7v4rlzxpq8NBZckTWrPlDwY2I/edit#slide=id.p

## 📽️ Data Cleaning and Wrangling
### 📝 Description how dataset is cleaned
- Separation of Movies and TV Shows: We developed a solution to differentiate between movies and TV shows, which were mixed in the dataset.
- Handling Duplicates: We merged duplicate rows from the API dataset and a Kaggle dataset.
- Formatting Issues: Special character formatting errors (e.g., 'Ã') were resolved.
- Column Reduction: Irrelevant columns, such as 'Poster' and 'Review_count,' were dropped to streamline our analysis.
- Column Reordering: We reorganized columns to improve readability and better align with our hypothesis.
- Handling Missing Data: Rows with missing or empty 'BoxOffice' values were removed.

## 🔥 Project Structure
This is a python project has below mentioned files.
- main.ipnyb - Main file is the main file which calls the functions defined in functions.py file and returns the clean data file in csv format.
- functions.py - This file contains all the definations(functions) and the loagic defined.
- README.md - Describes what the project is, how it is structured and what changes are applied to get a clean data file.
- data_cleaning.ipynb - How the data is being cleand based on the Hypothesis logic
- omdb_data.csv.csv - How the clean data file looks
