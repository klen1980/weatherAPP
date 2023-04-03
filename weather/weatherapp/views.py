from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm



def index(request):
    error = ''
    appid = 'd4eacd794d45c4cf8e74d41cf25f5914'
    url_geo = 'http://api.openweathermap.org/geo/1.0/direct?q={}&limit=5&appid='+appid
    url_city = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid='+appid+'&units=metric'
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        city_name = request.POST.get('name')
        if form.is_valid():
            if City.objects.filter(name = city_name).exists():
                error = 'Такой город уже есть'
                print('already exist')
            else:
                form.save()
        else:
            error = "Проверьте введенные данные"

    form = CityForm()
    cities = City.objects.order_by('-id')
    all_city =[]
    for city in cities:
        res = requests.get(url_geo.format(city.name)).json()
        lat= res[0].get('lat')
        lon = res[0].get('lon')
        res_weather = requests.get(url_city.format(lat,lon)).json()
        city_info = {
            'city' : city.name,
            'temp' : res_weather['main']['temp'],
            'icon': res_weather['weather'][0]['icon']
            }

        all_city.append(city_info)

    context = {'all_info': all_city, 'form': form, 'error': error}
    return render(request, 'weather/index.html',context)

def delete(request, task_id):
    task = City.objects.get(id=task_id)
    task.objects.delete()

def homework(request):
    return render(request, 'weather/homework.html')

# Create your views here.
