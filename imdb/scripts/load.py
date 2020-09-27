from api.models import Movie
import pandas as pd 







def run():
    data = pd.read_csv("data/imdb_data.csv")

    #keys : name,year,rank,certificate,genre,duration,rating,description

    for i in range(len(data)):
        name = data['name'][i]
        year = data['year'][i]
        rank = data['rank'][i]
        certificate = str(data['certificate'][i])
#typecast to int
        duration = data['duration'][i].replace("min","")
        duration = int(duration)

        genre = data['genre'][i]
        genre = genre.replace("\n","")
        rating = float(data['rating'][i])
        description = data['description'][i]
        description = description.replace("\n","")

        m = Movie.objects.get_or_create(name=name,year=year,rank=rank,certificate=certificate,
        duration=duration,genre=genre,rating=rating,description=description)


        print("Created object no: "+ str(i))

