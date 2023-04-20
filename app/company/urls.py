from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DepartmentListView, EmployeeViewSet

employee_router = DefaultRouter()
employee_router.register(r"employees", EmployeeViewSet)

urlpatterns = [
    path("departments/", DepartmentListView.as_view()),
    path('', include(employee_router.urls)),
]

# urlpatterns += employee_router.urls
