from rest_framework import serializers
from myapi.models import movies
class moviesSerializer(serializers.ModelSerializer):
    
    class Meta:
        models=movies
        fields=('id','name','cast','duration','type','rating','image','review')