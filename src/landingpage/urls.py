"""landingpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/', 'newsletter.views.contact', name='contact'),
    url(r'^about/', 'landingpage.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^accounts/profile', 'landingpage.views.profile', name='profile'),
    url(r'^admin/', admin.site.urls),

    #url(r'^newsletter/', 'newsletter.views.home' , name='newsletterhome')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #do not do in production
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #do not do in production