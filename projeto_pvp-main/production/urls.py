from django.urls import path
from production.views import home


urlpatterns = [
    path('', home),

]
