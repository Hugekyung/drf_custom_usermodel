from django.urls import path, include
from rest_framework import routers

from accountapp import views


router = routers.DefaultRouter()
router.register(r'users', views.MyUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]