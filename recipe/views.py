from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.context_processors import csrf

import requests
import json

def index(request):
	"""rstr = "http://api.yummly.com/v1/api/recipes?_app_id=8397ddf3&_app_key=5ddd5532a314c79efcb9e7cede1b98a5"
	rstr += "&allowedIngredient[]=bread&allowedIngredient[]=yogurt"
	rstr += "&allowedIngredient[]=bread&allowedIngredient[]=bread"
	r = requests.get(rstr)
	yummly = r.json()
	return HttpResponse(yummly["attribution"]["html"])"""
	template = loader.get_template('recipe/index.html')
	context = RequestContext(request, {  
	})
	return HttpResponse(template.render(context))

def showrecipe(request):
	if request.method != 'POST':
		return HttpResponse("Method didn't equal post")
	"""	
	rstr = "http://api.yummly.com/v1/api/recipes?_app_id=8397ddf3&_app_key=5ddd5532a314c79efcb9e7cede1b98a5"
	for key in request.POST :
		if len(key) >= 10 and key[:10] == "ingredient" :
			rstr += "&allowedIngredient[]="
			rstr += request.POST[key]
	r = requests.get(rstr)
	yummly = r.json()

	recipes = yummly["matches"]
	sample = recipes[0]
	
	template = loader.get_template('recipe/page2.html')
	context = RequestContext(request, {  
		'recipename1': sample["recipeName"],
		'picture1' : sample["smallImageUrls"][0],
		'rating1' : sample["rating"],
		'ingredients1' : sample["ingredients"],
		'link1' : "http://www.yummly.com/recipe/" + sample["id"],
		'bottom html' : yummly["attribution"]["html"],
	})
	"""
	template = loader.get_template('recipe/page2.html')
	context = RequestContext(request, {  
		'recipename1': "Caramelized Onion Dip",
		'picture1' : "http://lh6.ggpht.com/Y7bgTZe43hhFOQWDTnDa991bt0NpA9GmY0AZRBum2nsbkRPZXh9pdYf0bm6RSj7x8NRlds_Dmnyfwy_bu4AkaA8=s90",
		'rating1' : 5,
		'ingredients1' : ["unsalted butter","sandwich bread","bacon","shredded cheddar cheese","large eggs","pepper","salt"],
		'link1' : "http://www.yummly.com/recipe/Caramelized-onion-dip-308832",
		'bottom html' : "Recipe search powered by <a href='http://www.yummly.com/recipes'><img alt='Yummly' src='http://static.yummly.com/api-logo.png'/></a>",
	})

	return HttpResponse(template.render(context))