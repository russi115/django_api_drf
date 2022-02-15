from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('drf/', views.root),

    path('drf/vticket/', views.vticket, name='vticket'),
    path('drf/crud/', views.crud, name='crud'),

    path('drf/list/', views.getData ),
    path('drf/list/<int:id>', views.getData, name='getData'),

    path('drf/add/', views.addItem, name=""),

    path('drf/delete/<int:id>', views.deleteItem, name=""),

    path('drf/update/<int:id>', views.updateItem, name=""),

    path('drf/validate/<int:code>', views.validate, name="validate"),
]