from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# # class BuildUserInformation(models.Model):
# #     first_name = models.NullBooleanField('first name', False)
# #     last_name = models.NullBooleanField('last name', False)

class Website(models.Model):
    url = models.CharField(max_length=1000, null=True)