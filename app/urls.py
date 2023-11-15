"""
URL configuration for askexperts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page>', views.index, name='index_paginated'),
    path('question/<int:question_id>', views.onequestion, name='question'),
    path('page/<int:page>', views.onequestion, name='question_paginated'),
    path('login', views.login, name='login'),
    path('signup', views.registration, name='registration'),
    path('tag', views.taglist, name='taglist'),
    path('ask', views.newquestion, name='newquestion'),
    path('settings', views.settings, name='settings'),
    path('hot', views.hotquestions, name='hotquestions'),
    path('page/<int:page>', views.hotquestions, name='hotquestions_paginated'),
    path('admin/', admin.site.urls),
]