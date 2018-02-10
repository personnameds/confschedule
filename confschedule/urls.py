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

from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views

##Development server only
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('homepage.urls')),
    path('add/', include('classlists.urls')),
    
    path('<int:klass_id>/', include('schedule.urls')),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, {'next_page':'/'}, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('oauth2/', include('oauth2.urls')),
    path('admin/', admin.site.urls),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
