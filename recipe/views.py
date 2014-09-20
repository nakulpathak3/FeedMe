from django.shortcuts import render
from django.http import HttpResponse

import requests
import json


def index(request):
    r = requests.get("http://api.yummly.com/v1/api/recipes?_app_id=8397ddf3&_app_key=7fb261378fd34d8a3bdaa9a854b13e13&allowedIngredient[]=bread&allowedIngredient[]=yogurt")
    yummly = r.json()
    return HttpResponse(yummly["attribution"]["html"])
