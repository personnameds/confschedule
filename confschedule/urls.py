"""confschedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" Version 2.0 will need to check settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
#from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('homepage.urls')),
    url(r'^add/', include('classlists.urls')),
    url(r'^(?P<klass>\d+)/', include('schedule.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, {'next_page':'/'}, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
#    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
