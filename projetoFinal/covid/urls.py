from django.urls import path
from .views import *

urlpatterns = [
	path('teste/', page, name='page'),
]
