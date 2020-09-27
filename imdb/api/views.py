
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from rest_framework import views
from rest_framework.views import APIView


from rest_framework import generics

# Create your views here.

    
    

    


    



@api_view(["GET"])

def home(request):
    if request.method=="GET":
        order = request.query_params.get("order_by")
        
        print(order)
        
       

        if order is not None:
            order = order.split(",")


            #sort by name
            if order[0]=='name' and order[1]=='asc': ##descending order
                movies = Movie.objects.order_by('name')
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)

            if order[0] =='name' and order[1]=='dsc':
                movies = Movie.objects.order_by('-name')
                print(movies[0].name)
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)


            #sort by rating
            if order[0] =='rating' and order[1]=='dsc':
                movies = Movie.objects.order_by('-rating')
                print(movies[0].name)
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)
            if order[0] =='rating' and order[1]=='asc':
                movies = Movie.objects.order_by('rating')
                print(movies[0].name)
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)

            #sort by year    
            if order[0] =='year' and order[1]=='asc':
                movies = Movie.objects.order_by('year')
                print(movies[0].name)
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)
            if order[0] =='year' and order[1]=='dsc':
                movies = Movie.objects.order_by('-year')
                print(movies[0].name)
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)


            #sort by duration    
            if order[0] =='duration' and order[1]=='dsc':
                movies = Movie.objects.order_by('-duration')
                print(movies[0].name)
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)
            if order[0] =='duration' and order[1]=='asc':
                movies = Movie.objects.order_by('duration')
                print(movies[0].name)
                serial = MovieSerializer(movies,many=True)
                return Response(serial.data)


                    
            
        elif order is None: ##set default ordering to none if no params are present in URL
            movies = Movie.objects.all()
            serial = MovieSerializer(movies,many=True)
            return Response(serial.data)



class SearchView(APIView):
    

    def get(self,request):
        name = request.query_params.get("name")
        desc = request.query_params.get("desc")

        if name is not None:
            print(name)
            movies = Movie.objects.filter(name__icontains=name)
            serial = MovieSerializer(movies,many=True)
            return Response(serial.data)
        elif desc is not None:
            print(type(desc))
            movies = Movie.objects.filter(description__icontains=desc)
            serial = MovieSerializer(movies,many=True)
            return Response(serial.data)
        else:
            return Response({"message":"invalid query params, please enter 'name' or 'desc'"})    


                   


    