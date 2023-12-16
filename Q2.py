# Q2
import pandas as pd

# Sample IMDb dataset
data = {'Title': ['Marybeth', 'Matrix', 'Inception', 'Avatar'],
        'Year': [1978, 1999, 2010, 2009]}

imdb_df = pd.DataFrame(data)

def count_vowels_in_column(column):
    return column.str.lower().str.count('[aeiou]')


imdb_df['Vowels'] = count_vowels_in_column(imdb_df['Title'])

print(imdb_df)
