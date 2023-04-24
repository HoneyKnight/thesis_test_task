from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DepartmentListView, EmployeeViewSet, ProjectsViewSet

employee_router = DefaultRouter()
employee_router.register(r"employees", EmployeeViewSet)
employee_router.register(r"projects", ProjectsViewSet)

urlpatterns = [
    path("departments/", DepartmentListView.as_view()),
    path('', include(employee_router.urls)),
]

# urlpatterns += employee_router.urls
