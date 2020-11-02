"""alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="Login"),
    path('Logout', views.logout, name="Logout"),
    path('Home', views.home, name="Home"),
    path('Notice', views.notice, name="Notice"),
    path('Event', views.event, name="Event"),
    path('Job-Board', views.job, name="Job"),
    path('Search', views.search, name="search"),
    path('Gallery', views.gallery, name="Gallery"),
    path('Delete-Notice/<int:id>', views.delete_notice, name="Delete-Notice"),
    path('Delete-Event/<int:id>', views.delete_event, name="Delete-Event"),
    path('Delete-Gallery/<int:id>', views.delete_gallery, name="Delete-Gallery"),
    path('Delete-Job/<int:id>', views.delete_job, name="Delete-Job"),
    path('Delete-Alumni/<int:id>', views.delete_alumni, name="Delete-Alumni"),
    path('View-Profile/<int:id>', views.view_profile, name="Viewprofile"),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
