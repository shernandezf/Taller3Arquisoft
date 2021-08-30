from django.urls.conf import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns=[
   path('id_measurements/<id>/',views.get_id_measurements, name='measurements_id'),
   path('list_measurements/', views.get_measurements, name='measurements_List'),
   path('modificar_measurements/<id_modificado>/<str:Unit>/',views.modificando,name='modificado_measurment'),
   path('eliminar_measurements/<id_borrado>/',views.deleteMeasurments,name='eliminado_measurment')
]