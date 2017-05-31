from django.conf.urls import url,include

from . import views as v
from blog import views as b
# Create your views here.
urlpatterns=[
	url(r'^$',v.home,name='home'),
	url(r'^ggg',b.post_new,name='post_new'),
	url(r'^b',v.login,name='login'),
	url(r'^x',v.x,name='x'),
]
