from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
     path('', RedirectView.as_view(url='/admin/', permanent=False)), # this will redirect directly to the admin login page
    path('admin/', admin.site.urls), #or this path will redirect to admin login http://127.0.0.1:8000/admin/ 
    path('services/', include('services.urls')),
]
