from django.shortcuts import render
from django.http import JsonResponse

def get_data(request):
    data = [i for i in range(10)]
    return JsonResponse(data, safe=False)

