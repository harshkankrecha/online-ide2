
from django.conf.urls import url
from ide import views

urlpatterns = [
	url(r'^$',views.greetings),
    url(r'^home/run$',views.runcode),
]
