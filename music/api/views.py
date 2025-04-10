from django.shortcuts import render

from rest_framework import generics
from .models import Label,Artist
from .serializers import LabelSerializer, ArtistSerializer

class LabelList(generics.ListCreateAPIView):

    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class LabelDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class LabelArtistsList(generics.ListCreateAPIView):
    
    serializer_class = ArtistSerializer

    def get_queryset(self):
        label_id = self.kwargs['label_id']
        return Artist.objects.filter(label_id = label_id)


class ArtistList(generics.ListCreateAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class TopTenArtists(generics.ListAPIView):

    serializer_class = ArtistSerializer

    def get_queryset(self):
        return Artist.objects.order_by('-income')[:10]