# django
from django.urls import path
# views
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
