# IMDB-API
IMDB API made using Django Rest Framework


*Usage:

**To sort the  movies by rating,year,duration,name(alphabetical order) in Ascending and Descending forms:


http://localhost:8000/api?order_by=name,asc (name,ascending)
http://localhost:8000/api?order_by=name,dsc (name,descending)
http://localhost:8000/api?order_by=rating,asc(rating,ascending)
http://localhost:8000/api?order_by=rating,dsc(rating,descending)
http://localhost:8000/api?order_by=year,asc(year,ascending)
http://localhost:8000/api?order_by=year,dsc(descending)
http://localhost:8000/api?order_by=duration,asc(duration,ascending)
http://localhost:8000/api?order_by=name,asc(duration,descending)


**To search for movies either by name or description:

***Search by name
http://localhost:8000/api/search?name=Godfather

***Search by description
http://localhost:8000/api/search?desc=Vito




