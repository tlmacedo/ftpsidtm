from django.conf.urls import url
from cafeperfeito import views

urlpatterns = [
    #    url(r'^$', views.index, name='index'),
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    #    url(r'^certificado/$', views.certificado, name='certificado')
]
