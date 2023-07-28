from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import Menu_Item, Ingredient
from django.core import serializers
from django.forms.models import model_to_dict


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def full_menu(request):
    try:
        data = [i.json() for i in Menu_Item.objects.all()]      #Calling json method on Menu_Item and looping through
        return HttpResponse(json.dumps(data), content_type="application/json")  #Returning http response. json.dumps parses to jason
        #Checking if Menu_item model does not exist and raises error if true
    except Menu_Item.DoesNotExist:
        errmsg = "Does not exist"
        raise err(errmsg)