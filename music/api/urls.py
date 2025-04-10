from django.urls import path
from .views import(
    LabelList, LabelDetail, ArtistList, ArtistDetail, TopTenArtists, LabelArtistsList
)

urlpatterns = [
    path('labels/', LabelList.as_view(), name = 'label-list'),
    path('labels/<int:pk>/', LabelDetail.as_view(), name = 'label-detail'),
    path('labels/<int:label_id>/artists/', LabelArtistsList.as_view(), name = 'label-artists'),

    path('artists/', ArtistList.as_view(), name = 'artist-list'),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name = 'artist-detail'),

    path('artists/top_ten/', TopTenArtists.as_view(), name  = 'top-ten-artists')    

]