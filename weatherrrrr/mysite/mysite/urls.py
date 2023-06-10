"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('continentsAll/', views.ContinentList.as_view({'get': 'list'})),

    path('continents/<str:continent_name>/', 
        views.ContinentList.as_view({'get': 'list'})),

    path('continents/<str:continent_name>/<str:country_name>/<str:city_name>/', 
        views.ContinentList.as_view({'get': 'retrieve'})),

    path('continents/<str:continent_name>/<str:country_name>/', 
        views.ContinentList.as_view({'get': 'list'})),

    path('countries/', views.CountryList.as_view()),
    path('city/', views.CityList.as_view()),
    path('date/', views.DateList.as_view()),
    path('sky/', views.SkyList.as_view()),
    path('temp/', views.TempList.as_view()),
    path('timeRise/', views.TimeRiseList.as_view()),
    path('timeSet/', views.TimeSetList.as_view()),
    path('attent/', views.AttentList.as_view()),
    path('dateweather/', views.DateWeatherList.as_view()),
    path('timeweather/', views.TimeWeatherList.as_view()),
    path('timeweather6/', views.TimeWeather6List.as_view()),
    path('timeweather9/', views.TimeWeather9List.as_view()),
    path('timeweather12/', views.TimeWeather12List.as_view()),
    path('timeweather15/', views.TimeWeather15List.as_view()),
    path('timeweather20/', views.TimeWeather20List.as_view()),
    path('timeweather23/', views.TimeWeather23List.as_view()),
]