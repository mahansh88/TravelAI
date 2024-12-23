from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .filters import GroupFilter, UserFilter
from .models import CustomGroup, CustomUser, Rating, Request, Trip
from .serializers import (
    GroupSerializer,
    RatingSerializer,
    RequestSerializer,
    TripSerializer,
    UserSerializer,
)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.select_related("group").all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ["min_participants", "max_participants", "name"]
    ordering_fields = ["name", "min_participants", "max_participants"]
    ordering = ["name"]  # Default ordering
    filterset_class = GroupFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomGroup.objects.all()
        else:
            return CustomGroup.objects.filter(status=True)


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
