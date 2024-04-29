from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def me(request):
    return JsonResponse({
        'user': {
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email
        }
    })


@permission_classes([AllowAny])
@api_view(["POST",])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
@api_view(["POST",])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Account has been created'

            data['user'] = {
                'id': str(account.id),
                'username': str(account.username),
                'email': str(account.email),
            }

            refresh = RefreshToken.for_user(account)
            data['data'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)
