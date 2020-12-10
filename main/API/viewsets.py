from rest_framework import viewsets, permissions
from main.models import HealthCheck
from .serializers import HealthCheckSerializer, UserSerializer
from .permissions import	IsOwner
from rest_framework.response import Response
from main.models import	User
from rest_framework import mixins


class HealthCheckViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = HealthCheck.objects.all()
    serializer_class = HealthCheckSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OwnHealthCheckViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = HealthCheck.objects.none()

	def list(self, request):
		queryset = HealthCheck.objects.filter(user=self.request.user)
		serializer = HealthCheckSerializer(queryset, many=True)
		return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer