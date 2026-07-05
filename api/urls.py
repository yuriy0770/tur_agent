from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('api/', views.CategoryApi.as_view(), name='api')
]
