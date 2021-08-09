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
""" 
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    ModelViewSet은 View --> APIView --> GenericAPIView --> GenericViewSet에 이르기까지의
    모든 View를 상속하는 모델로서 아래 두줄의 코드로 위 모든 기능을 한꺼번에 간단히 구현 가능하다.
    
    - create (method POST, 생성)

    - list (method GET, 리스트)

    - retrieve (method GET, Detail 특정 pk ex) posts/<int:pk>/)

    - update (method PUT)

    - partial_update (method PATCH)

    - destroy (method DELETE)
"""
class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MyUserSerializer
    queryset = models.MyUser.objects.all()
