from rest_framework import serializers
from .models import Movie



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
         #keys : name,year,rank,certificate,genre,duration,rating,description
        fields = ('name','year','rank','certificate','genre','duration','rating','description')