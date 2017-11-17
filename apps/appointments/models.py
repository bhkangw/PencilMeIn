from __future__ import unicode_literals
from django.db import models
from datetime import date
from datetime import datetime
from ..login.models import User
from datetimewidget.widgets import DateTimeWidget


class AppointmentManager(models.Manager):
    def appointment_validator(self, postData):
        response = {'status': True, 'errors': []}
        if len(postData['task']) < 1:
            response['errors'].append("Tasks field cannot be empty!")
        if len(postData['date']) < 9:
            response['errors'].append("Must select valid date!")
        if len(response['errors']) == 0:
            return response
        else:
            response['status'] = False
        return response

    def sorted(self):
        return (self.all().order_by('-date'))


class Appointment(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    date = models.DateField(blank=False)
    user = models.ForeignKey(User, related_name="appointment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AppointmentManager()

    def is_today(self):
        # return date.today().strftime("%Y-%m-%d") == self.date
        return {'date': datetime.now()}


# class yourForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         widgets = {
#             #Use localization and bootstrap 3
#             'datetime':
#             DateTimeWidget(
#                 attrs={'id': "date"}, usel10n=True, bootstrap_version=3)
#         }