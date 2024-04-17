# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer

def companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many = True)
    return JsonResponse(serializer.data, safe=False)

def companies_by_id(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error' : str(e)}, status = 400)
    
    serializer = CompanySerializer(company)
    return JsonResponse(serializer.data, safe=False)

def vacancies_by_companies(request, id): 
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error' : str(e)}, status = 400)
    
    vacancies = Vacancy.objects.filter(company=company)
    serializer = VacancySerializer(vacancies, many = True)
    return JsonResponse(serializer.data, safe=False)

def vacancies(requset):
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many = True)
    return JsonResponse(serializer.data, safe=False)

def vacancies_by_id(request, id):
    try: 
        vacancy = Company.objects.get(id=id)
        serializer = CompanySerializer(vacancy)
        return JsonResponse(serializer.data, safe=False)
    except Company.DoesNotExist as e:
        return JsonResponse({
            'error' : str(e)
        })

def top_ten(requset):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many = True)
    return JsonResponse(serializer.data, safe = False)