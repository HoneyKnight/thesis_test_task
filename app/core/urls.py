from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/docs/", include("swagger.urls")),
    path("api/company/", include("company.urls")),
]
