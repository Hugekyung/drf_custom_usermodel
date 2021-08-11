from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from accountapp import models
from accountapp import serializers
from accountapp import permissions


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
"""
    - authentication_classes와 permission_classes를 적용하는 방법에는 2가지가 있다. 1) settings에서 전역 설정하는 방법 2) 각 View 별로 설정하는 방법
    - 아래의 경우 settings에서 별도로 설정하지 않고 View별로 다른 설정을 해줬다.
    - 앱의 성격과 접근 권한의 상황 등에 따라 다르게 설정하면 된다.
    - (TokenAuthentication,)와 같이 콤마를 꼭 적어야 오류가 안난다.
"""
"""
    현재 문제: 메인페이지에서 로그인 후 다른 페이지로 넘어갈 때 로그인 유지가 안됨.
"""
class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MyUserSerializer
    queryset = models.MyUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class BlogItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BlogItemSerializer
    queryset = models.BlogItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnBlogItem,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES