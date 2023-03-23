from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def perform_math_operations(request):
    a = request.data.get('a')
    b = request.data.get('b')

    addition = a + b
    substraction = a - b
    multiplication = a * b
    division = a / b

    result = {
        'addition': addition,
        'substraction': substraction,
        'multiplication': multiplication,
        'division': division,
    }

    return Response(result)

