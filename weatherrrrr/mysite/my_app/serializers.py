from rest_framework import serializers
from .models import Continent, Country, City, Date, Sky,Temp, TimeRise, TimeSet, Attent, DateWeather, TimeWeather, TimeWeather6, TimeWeather9, TimeWeather12, TimeWeather15, TimeWeather20, TimeWeather23

class DateWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateWeather
        fields = ['timeWeather', 'timeWeather6', 'timeWeather9', 'timeWeather12', 'timeWeather15', 'timeWeather20', 'timeWeather23', 'timeRise', 'timeSet', 'atttent_name']

class TimeWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather
        fields = ['time', 'temp', 'sky']

class TimeWeather6Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather6
        fields = ['time', 'temp', 'sky']

class TimeWeather9Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather9
        fields = ['time', 'temp', 'sky']

class TimeWeather12Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather12
        fields = ['time', 'temp', 'sky']

class TimeWeather15Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather15
        fields = ['time', 'temp', 'sky']

class TimeWeather20Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather20
        fields = ['time', 'temp', 'sky']

class TimeWeather23Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather23
        fields = 'time', 'temp', 'sky'

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['date']

class SkySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sky
        fields = ['sky']

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ['__all__']

class TimeRiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeRise
        fields = ['timeRise']

class TimeSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSet
        fields = ['timeSet']

class AttentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attent
        fields = ['atttent_name']

class CitySerializer(serializers.ModelSerializer):
    dateweather = DateWeatherSerializer(many=True, read_only=True)
    fields = '__all__'
    class Meta:
        model = City
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    city = CitySerializer(many=True, read_only=True)
    fields = '__all__'
    class Meta:
        model = Country
        fields = '__all__'

class ContinentSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)
    fields = '__all__'
    class Meta:
        model = Continent
        fields = '__all__'




