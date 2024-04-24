
'''from django.contrib import admin
from django.urls import path,include

urlpatterns =[
    path('admin/', admin.site.urls),
    #includingi urls.py file routing
    path('api/',include('api.urls')),
]
'''
# project_name/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API URLs from the 'api' app
]

