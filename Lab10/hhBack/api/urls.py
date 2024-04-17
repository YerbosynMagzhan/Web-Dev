from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.companies),
    path('companies/<int:id>/', views.companies_by_id),
    path('companies/<int:id>/vacancies', views.vacancies_by_companies),
    
    path('vacancies/', views.vacancies),
    path('vacancies/<int:id>/', views.vacancies_by_id),
    path('vacancies/top_ten/', views.top_ten),
]