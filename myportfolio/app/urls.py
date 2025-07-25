from django.urls import path
from .views import HomeView, MonCView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cv/', MonCView.as_view(), name='cv'),
]
