from django.contrib import admin
from django.urls import path
from movieApp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/directors', DirectorAPIList.as_view()),
    path('api/v1/directors/<int:pk>', DirectorAPIRetrieve.as_view()),
    path('api/v1/movie', MovieAPIList.as_view()),
    path('api/v1/movie/<int:pk>', MovieAPIRetrieve.as_view()),
    path('api/v1/review', ReviewAPIList.as_view()),
    path('api/v1/review/<int:pk>', ReviewAPIRetrieve.as_view()),

]
