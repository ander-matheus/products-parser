from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import SignInSerializer, UserSerializer


class SignInView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.django_user
            refresh = RefreshToken.for_user(user)
            result = UserSerializer(user).data
            result.update(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
            return Response(result)
