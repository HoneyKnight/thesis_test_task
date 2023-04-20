from django.db.models import Count, Sum
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class CreateRetrieveDestroyViewSet(
    ListModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    pass


class DepartmentListView(ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.annotate(
            employees_count=Count('employees')
        ).annotate(employees_total_salary=Sum('employees__salary'))


class EmployeeViewSet(CreateRetrieveDestroyViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['last_name', 'department__id']
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
