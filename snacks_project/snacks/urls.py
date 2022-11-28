from django.urls import path
from .views import home_page, about_page

urlpatterns = [
    path('', home_page.as_view(), name='home'),
    path('about/', about_page.as_view(), name='about'),
]
