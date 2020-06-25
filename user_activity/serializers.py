from rest_framework import serializers
from .models import UserModel, UserActivityModel


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('id', 'real_name', 'tz',)


class UserActivitySerializer(serializers.ModelSerializer):
	user = UserSerializer()
	
	class Meta:
		model = UserActivityModel
		fields = ('start_time', 'end_time', 'user')
