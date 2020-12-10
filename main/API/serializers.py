from rest_framework import serializers
from main.models import HealthCheck, User


class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ['NHS_no', 'id', 'first_name', 'last_name', 'healthcheck_set']


class HealthCheckSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = HealthCheck
		fields = ['age', 'height', 'weight', 'smoking', 'alcohol']
