"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from caam import views 
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("", views.index),
    path('animal/<int:id>/', views.animal),
    path("admin/", admin.site.urls),
 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-success/', views.logout_success_view, name='logout_success'),
    path('animal/novo/', views.criar_animal , name='criar_animal'),
    path('adotar/<int:id>/', views.adotar_animal, name='adotar_animal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root="static")
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    