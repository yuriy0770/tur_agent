from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tour/<slug:slug>/', views.CountryDetailView.as_view(), name='country_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('tour/<slug:slug>/review/', views.add_review, name='add_review'),
]