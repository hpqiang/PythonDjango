from django.conf.urls import url

from . import views

from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
	#ex: /my_sci/
	#url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^$', views.index, name='index'),
] 