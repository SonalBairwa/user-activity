from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^user-activity/$', views.UserActivityView.as_view(), name='user_activity')
]