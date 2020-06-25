from django.db import models
from utils.general_methods import GeneralMethods


class BaseModel(models.Model):
	# Always add current timestamp when new entry added
	added_on = models.DateTimeField(auto_now_add=True)

	# Always add current timestamp when entry updated
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
		ordering = ('-added_on')


class UserModel(BaseModel):
	id = models.CharField(max_length=255, primary_key=True)
	real_name = models.CharField(max_length=255)
	tz = models.CharField(max_length=255, help_text='Timezone')

	def __str__(self):
		return self.real_name


	class Meta:
		db_table = 'users'
		verbose_name = 'User'
		verbose_name_plural = 'Users'

	def save(self, *args, **kwargs):
		# Generate Id before saving
		if not self.id:
			self.id = GeneralMethods.random_alphanumeric(string_length=10, caps=True)
		# Handle duplicate id later
		super(UserModel, self).save(*args, **kwargs)


class UserActivityModel(BaseModel):
	id = models.BigAutoField(primary_key=True)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_activity_user')

	def __str__(self):
		return str(self.id)

	class Meta:
		db_table = 'user_activity'
		verbose_name = 'User Activity'
		verbose_name_plural = 'User Activities'

