from django.urls import path
from .views import WheelSpecificationAPIView
 
 
urlpatterns = [
 path('forms/wheel-specifications', WheelSpecificationAPIView.as_view(), name='wheel-specifications'),
 ]