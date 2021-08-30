from measurements.models import Measurement
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_idmeasurement
from .logic.logic_measurements import modify_measurement
from .logic.logic_measurements import delete_measurements
def get_id_measurements(request,id):
    measurement_id=get_idmeasurement(id)
    measurement_id_json=serializers.serialize('json',measurement_id)
    return HttpResponse(measurement_id_json, content_type='application/json')
    
def get_measurements(request):
    measurement=get_all_measurements()
    measurements_list=serializers.serialize('json',measurement)
    return HttpResponse(measurements_list, content_type='application/json')


def modificando(request,id_modificado,Unit):
    modify_measurement(id_modificado,Unit)
    return HttpResponse('<h1> se ha modificado el measurments con el id: '+id_modificado + '<h1>' )
       
def deleteMeasurments(request,id_borrado):
    delete_measurements(id_borrado)
    return  HttpResponse('<h1> se ha borrado el measurments con el id: '+id_borrado + '<h1>' )