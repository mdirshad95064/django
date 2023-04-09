from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('blog/', blog, name='blog'),
    path('blog/', blog, name='blog'),
    path('pages', pages, name='pages'),
    path('contact', contact, name='contact'),
]