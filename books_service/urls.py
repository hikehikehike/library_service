from django.urls import path, include
from rest_framework import routers

from books_service.views import BookViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "books_service"
