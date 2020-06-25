from django.views import View
from rest_framework.views import APIView
from utils.general_methods import GeneralMethods
from rest_framework.generics import ListAPIView
from .serializers import UserActivitySerializer
from .models import UserActivityModel
import datetime


class UserActivityView(ListAPIView):

	""" Description : To see list of users and their activity period """
	
	gm = GeneralMethods()
	serializer_class = UserActivitySerializer
	queryset = UserActivityModel.objects.select_related()

	

	def list(self, *args, **kwargs):
		
		response = super(UserActivityView, self).list(*args, **kwargs)
		result = dict()
		for item in response.data:
			_id = item.get('user').get('id')
			if _id not in result:
				result.update({_id: dict(activity_periods=list())})
				result[_id].update({
					**item.get('user'),
				})
			result[_id]['activity_periods'].append({
				'start_time':datetime.datetime.strptime(item.get('start_time'), '%Y-%m-%dT%H:%M:%SZ').strftime("%b %d %Y"),
				'end_time': datetime.datetime.strptime(item.get('end_time'), '%Y-%m-%dT%H:%M:%SZ').strftime("%b %d %Y"),
			})

		return self.gm.success_response(result.values())

