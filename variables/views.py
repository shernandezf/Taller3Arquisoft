from variables.models import Variable
from django.shortcuts import render
from .Logic.logic_variables import get_all_variables
from django.http import HttpResponse
from django.core import serializers

def get_variables(request):
    Variables=get_all_variables()
    Variable_list=serializers.serialize('json',Variables)
    return HttpResponse(Variable_list, content_type='application/json')
# Create your views here.
