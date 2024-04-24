'''from django.urls import path
from . import views
urlpatterns =[
     #url path for predict view
    path('predict/',views.predict,name='predict'),
    ]

'''
# api/urls.py
from django.urls import path
from .views import predict

urlpatterns = [
    path('predict/', predict, name='predict'),
]
