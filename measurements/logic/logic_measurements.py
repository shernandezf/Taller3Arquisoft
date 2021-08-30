
import measurements
from ..models import Measurement

def get_all_measurements():
    measurements=Measurement.objects.all()
    return measurements
def  get_idmeasurement(id):
    measurements=Measurement.objects.filter(pk=id)
    return measurements
def modify_measurement(id,Unit):
    Measurement.objects.filter(pk=id).update(unit=Unit)
def delete_measurements(id):
    Measurement.objects.filter(pk=id).delete()    