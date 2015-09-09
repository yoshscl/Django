"""general URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from adray import views
#for wizard
from django.conf.urls import patterns
from adray.forms import ContactForm1, ContactForm2
from adray.views import ContactWizard


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
   url(r'^$', views.index, name='home'),
    url(r'^input_data', views.insert_data_form, name='input_data'),

     url(r'^simulate/$', views.simulate, name='simulate'),
    url(r'^existing/$', views.existing, name='existing_tests'),
    url(r'^existing/(?P<existing_test>.+)/$', views.specific_test,name='test-existing_test'),
     url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2])),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
]

