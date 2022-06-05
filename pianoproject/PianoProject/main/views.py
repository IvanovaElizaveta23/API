import json, requests
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer



def index(request):


 #   response = request.GET
  #  print(response)
 #   json_format = response.text
  #  obj = JSONRenderer().render(json_format)
  #  print(obj)

    response = requests.get("http://127.0.0.1:8000/api/products")
    json_format = response.text
    obj = json.loads(json_format)
    print(obj)
    data = {
        'title': 'Главная страница',
        'data': obj,
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
