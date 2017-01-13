from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from math import pi

# Create your models here.
class Input(models.Model):
	A = models.FloatField(verbose_name=' amplitude(m) ', default=1.0)
	b = models.FloatField(verbose_name=' damping co(kg/s) ', default=0.0)
	w = models.FloatField(verbose_name=' frequency(1/s) ', default=2*pi)
	T = models.FloatField(verbose_name=' time interval(s) ', default=18)

class InputForm(ModelForm):
	class Meta:
		model = Input
		fields = '__all__' # refer to: http://stackoverflow.com/questions/28306288/removedindjango18warning-creating-a-modelform-without-either-the-fields-attri