from django.urls import path,include
from watch_list.api.views import movie_list,movie_deatils
urlpatterns = [
    path('list/', movie_list,name='movie-list'),
    path('<int:pk>/', movie_deatils,name='movie-deatils'),

]
