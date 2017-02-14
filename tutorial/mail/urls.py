from django.conf.urls import url

from . import views

app_name='mail'
urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^store/', views.store,name='store'),
	#url(r'^/results/$',views.results,name='results'),
]
