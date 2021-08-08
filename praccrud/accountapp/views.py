from django.shortcuts import render
from rest_framework import viewsets

from accountapp import models
from accountapp import serializers


"""
ViewSet을 사용하면 serializer_class나 queryset을 한번만 선언하면 여러 뷰에서 활용할 수 있다.
즉, View을 사용할 때보다 반복적인 코드사용을 최소화할 수 있다.
또한, URL conf에서 각각의 라우팅을 지정할 때도 ViewSet을 사용하면 직접 지정할 필요가 없다.
ViewSet은 일관된 대규모 API를 빠르게 구축할 수 있다는 장점이 있으며, View는 각각의 로직을 직접
커스터마이징할 수 있다는 점에서 장점이 있어 서로 Trade-Off 관계에 있다고 볼 수 있다.
"""
class MyUserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.MyUserSerializer
    queryset = models.MyUser.objects.all()
