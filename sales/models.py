from django.db import models
from django.utils import timezone


class SaleSumary(models.Model):

	order_date = models.DateField()
	region = models.CharField(max_length=10)
	rep = models.CharField(max_length=200)
	item = models.CharField(max_length=150)
	units = models.IntegerField()
	unit_cost = models.DecimalField(max_digits=6, decimal_places=2)
	total = models.IntegerField()
	created_on = models.DateTimeField(default=timezone.now, null=False)

	def __str__(self):
		"""
		This portion in essence is just iterating over the
		class properties and appending them to a string, so that in the event
		we want to print the object representation we get a human readable
		object representation
		"""
		return ', '.join(['{key}={value}'.format(
			key=key, value=self.__dict__.get(key)) for key in self.__dict__])

	class Meta:
		db_table = 'sales_summary'
		# enforces at the database that a rep should have unique order summary per given day
		unique_together = (('order_date', 'rep'),)
