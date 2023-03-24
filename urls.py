from django.urls import path
from . import views

urlpatterns = [
    # path('movies/', movies_list.as_view()),
    # path('movies/', movies_details.as_view()),
    path('movies_list/', views.movies_list, name='movies_list'),
    
    
]