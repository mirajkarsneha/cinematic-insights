import string
import numpy as np
import pandas as pd
import re

# Function to check if a title contains only numbers or special characters (no alphabets)
def is_only_numbers_or_special_chars(title):
    return bool(re.match(r'^[^a-zA-Z]+$', title))


# Function to standardize documentary genres
def standardize_documentry_genres(genre):
    if isinstance(genre, str):
        if 'Documentary' in genre:
            return 'Documentary'
    return genre

# Function to standardize animation genres
def standardize_animation_genres(genre):
    if isinstance(genre, str):
        # Replace specific animation genres with 'Animation'
        if 'Animation' in genre:
            return 'Animation'
    return genre
    
# Function to standardize animation genres
def standardize_biography_genres(genre):
    if isinstance(genre, str):
        # Replace specific animation genres with 'Animation'
        if 'Biography' in genre:
            return 'Biography'
    return genre

# Function to standardize animation genres
def standardize_adventure_genres(genre):
    if isinstance(genre, str):
        # Replace specific animation genres with 'Animation'
        if 'Adventure' in genre:
            return 'Adventure'
    return genre

# Function to check if a title contains only numbers or special characters (no alphabets)
def is_only_numbers_or_special_chars(title):
    # Regex to check if the title does NOT contain any alphabetic characters (only numbers and special characters)
    return bool(re.match(r'^[^a-zA-Z]+$', title))

# Function to extract runtime in minutes from the string
def extract_runtime(runtime_str):
    if isinstance(runtime_str, str):
        # Extract the numeric part of the runtime
        return int(runtime_str.split()[0])  # Convert to int
    return None

# Function to classify by runtime
def classify_by_runtime(runtime):
    if pd.isna(runtime):
        return 'Unknown'
        
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9069f7e-2b3b-4c2a-9404-cee0d88e1094",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
