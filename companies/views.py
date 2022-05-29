from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from .models import Company
from .serializers import ComapnySerializer, PostComapnySerializer


@permission_classes([IsAuthenticated])
class ComapnyViewSet(viewsets.ViewSet):
    """
    ComapnyViewSet for listing or retrieving Company.
    """
    def list(self, request):
        queryset = Company.objects.all()
        serializer = ComapnySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = ComapnySerializer(company)
        return Response(serializer.data)

    def create(self, request):
        user_data = request.data
        user_data['owner'] = int(get_current_user(request))
        serializer = PostComapnySerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Company saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({"massage": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def get_current_user(request):
    """
    Get user id from request
    """
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    try:
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user_id = valid_data['user_id']
        return user_id
    except ValidationError as v:
        print("validation error", v)