"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from polls import views

urlpatterns = [
	url(r'^$',views.IndexView.as_view(), name='home'), #MQ

	url(r'^polls/', include('polls.urls')),
	url(r'^my_sci/', include('my_sci.urls')),

    url(r'^admin/', admin.site.urls),
]

# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# if settings.DEBUG:
# 	urlpatterns+=static(settings.STATIC_URL, docement_root=settings.STATIC_URL)
# 	# urlpatterns+=staticfiles_urlpatterns()