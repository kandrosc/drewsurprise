"""drewsurprise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from surprise.views import firstday, secondday, thirdday, fourthday

urlpatterns = [
    path('admin/', admin.site.urls),
    path('I/', firstday, name="firstday"), # June 2nd
    path('appreciate/', secondday, name="secondday"), # June 6th
    path('you/', thirdday, name="thirdday"), # June 10th
    path('Drew/', fourthday, name="fourthday") # June 14th
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
