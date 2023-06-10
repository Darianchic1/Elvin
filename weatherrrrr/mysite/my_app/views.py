from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import ContinentSerializer, CountrySerializer, CitySerializer, DateSerializer, SkySerializer, TempSerializer, TimeRiseSerializer, TimeSetSerializer, AttentSerializer, DateWeatherSerializer, TimeWeatherSerializer, TimeWeather6Serializer, TimeWeather9Serializer, TimeWeather12Serializer, TimeWeather15Serializer, TimeWeather20Serializer, TimeWeather23Serializer
from .models import Continent, Country, City, Date, Sky, Temp, TimeRise, TimeSet, Attent, DateWeather, TimeWeather, TimeWeather6, TimeWeather9, TimeWeather12, TimeWeather15, TimeWeather20, TimeWeather23
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Prefetch

class ContinentListAll(APIView):
    def get(self, request, format=None):
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)
    
class ContinentList(viewsets.ViewSet):
    def list(self, request, continent_name=None):
        queryset = Continent.objects.all()
        user = get_object_or_404(queryset, continent_name=continent_name)
        serializer = ContinentSerializer(user)
        return Response(serializer.data)
    
    def retrieve(self, request, continent_name=None, country_name=None, city_name=None):
        if country_name and city_name:

            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    country_name=country_name).prefetch_related(
                    Prefetch("country", queryset=CountryList.objects.filter(city_name=city_name)))
                )
            )
        else: 
            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    country_name=country_name))
            )
        serializer = ContinentSerializer(queryset, many=True)

        return Response(serializer.data)
    
class CountryList(APIView):
    def get(self, request, format=None):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

class CityList(APIView):
    def get(self, request, format=None):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)  
    
class DateList(APIView):
    def get(self, request, format=None):
        date = Date.objects.all()
        serializer = DateSerializer(date, many=True)
        return Response(serializer.data)

class SkyList(APIView):
    def get(self, request, format=None):
        sky = Sky.objects.all()
        serializer = SkySerializer(sky, many=True)
        return Response(serializer.data)

    
class TempList(APIView):
    def get(self, request, format=None):
        temp = Temp.objects.all()
        serializer = TempSerializer(temp, many=True)
        return Response(serializer.data)
    
class TimeRiseList(APIView):
    def get(self, request, format=None):
        timeRise = TimeRise.objects.all()
        serializer = TimeRiseSerializer(timeRise, many=True)
        return Response(serializer.data)   
    
class TimeSetList(APIView):
    def get(self, request, format=None):
        timeSet = TimeSet.objects.all()
        serializer = TimeSetSerializer(timeSet, many=True)
        return Response(serializer.data)
    
class AttentList(APIView):
    def get(self, request, format=None):
        attent = Attent.objects.all()
        serializer = AttentSerializer(attent, many=True)
        return Response(serializer.data)
    
class DateWeatherList(APIView):
    def get(self, request, format=None):
        dateweather = DateWeather.objects.all()
        serializer = DateWeatherSerializer(dateweather, many=True)
        return Response(serializer.data)
    
class TimeWeatherList(APIView):
    def get(self, request, format=None):
        timeweather = TimeWeather.objects.all()
        serializer = TimeWeatherSerializer(timeweather, many=True)
        return Response(serializer.data)

class TimeWeather6List(APIView):
    def get(self, request, format=None):
        timeweather6 = TimeWeather6.objects.all()
        serializer = TimeWeather6Serializer(timeweather6, many=True)
        return Response(serializer.data)

class TimeWeather9List(APIView):
    def get(self, request, format=None):
        timeweather9 = TimeWeather9.objects.all()
        serializer = TimeWeather9Serializer(timeweather9, many=True)
        return Response(serializer.data)
    
class TimeWeather12List(APIView):
    def get(self, request, format=None):
        timeweather12 = TimeWeather12.objects.all()
        serializer = TimeWeather12Serializer(timeweather12, many=True)
        return Response(serializer.data)
    
class TimeWeather15List(APIView):
    def get(self, request, format=None):
        timeweather15 = TimeWeather15.objects.all()
        serializer = TimeWeather15Serializer(timeweather15, many=True)
        return Response(serializer.data)
    
class TimeWeather20List(APIView):
    def get(self, request, format=None):
        timeweather20 = TimeWeather20.objects.all()
        serializer = TimeWeather20Serializer(timeweather20, many=True)
        return Response(serializer.data)
    
class TimeWeather23List(APIView):
    def get(self, request, format=None):
        timeweather23 = TimeWeather23.objects.all()
        serializer = TimeWeather23Serializer(timeweather23, many=True)
        return Response(serializer.data)