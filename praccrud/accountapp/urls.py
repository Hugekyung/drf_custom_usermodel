from django.urls import path, include
from rest_framework import routers

from accountapp import views


router = routers.DefaultRouter() # DefaultRouter 클래스는 자동으로 API root view를 생성한다
router.register(r'users', views.MyUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]