from api.models import Movie
import pandas as pd 



data = pd.read_csv('api/data/imdb.csv')


print(data.info())



