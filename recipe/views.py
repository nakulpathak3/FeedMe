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
	rstr = "http://api.yummly.com/v1/api/recipes?_app_id=8397ddf3&_app_key=5ddd5532a314c79efcb9e7cede1b98a5"
	check = ""
	for key in request.POST :
		check += key
		check += "1"
		if key == "allowedIngredient[]" :
			rstr += "&allowedIngredient[]="
			rstr += request.POST[key]
	r = requests.get(rstr)
	yummly = r.json()

	recipes = yummly["totalMatchCount"]
	#sample = recipes[0]

	"""
	template = loader.get_template('recipe/page2.html')
	context = RequestContext(request, {  
		'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))
	"""
	"""
	4 recipes
	name
	picture
	rating
	ingredients
	link
	"""
	return HttpResponse(check)
	#return HttpResponse(yummly["attribution"]["html"])