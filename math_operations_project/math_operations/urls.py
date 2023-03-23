from django.urls import path
from .views import perform_math_operations

urlpatterns = [
    path('math-operations/', perform_math_operations),
]
