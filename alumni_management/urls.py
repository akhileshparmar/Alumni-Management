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

    path('', views.home, name="Home"),

    path('About', views.About, name="About"),

    path('Login', views.login, name="Login"),

    path('Logout', views.logout, name="Login"),

    path('Register', views.register, name="Register"),

    path('Email', views.email, name="Email"),

    path('Feedback', views.feedback, name="Feedback"),

    path('Notices', views.notices, name="Notices"),

    path('Events', views.events, name="Events"),

    path('Event-info/<int:id>', views.event_info, name="Event-info"),    

    path('Job-Board', views.job_board, name="Job-board"), 

    path('Job-info/<int:id>', views.job_info, name="Job-info"),

    path('Gallery', views.gallery, name="Gallery"),

    path('Image/<int:id>', views.image, name="Image"),

    path('View-Profile/<int:id>', views.view_profile, name="Viewprofile"),

    path('upload-image/<int:id>', views.upload_image, name="Uploadimage"),

    path('edit-profile/<int:id>', views.edit_profile, name="Editprofile"),

    path('update-credentials/<int:id>', views.update_credentials, name="Updatecredentials"),

    #path('Send-Email', views.Send_Email, name="Send-Email"),





    path('Admin', views.Admin_login, name="Admin-login"),
    path('Admin-Logout', views.Admin_logout, name="Admin-logout"),
    path('Admin-Home', views.Admin_Home, name="Admin-Home"),
    path('Admin-Notice', views.Admin_Notice, name="Admin-Notice"),
    path('Admin-Event', views.Admin_Event, name="Admin-Event"),
    path('Admin-Job-Board', views.Admin_Job, name="Admin-Job"),
    path('Admin-Search', views.Admin_Search, name="Admin-Search"),
    path('Admin-Gallery', views.Admin_Gallery, name="Admin-Gallery"),
    path('Admin-Email', views.Admin_Email, name="Admin-Email"),
    path('Delete-Notice/<int:id>', views.delete_notice, name="Delete-Notice"),
    path('Delete-Event/<int:id>', views.delete_event, name="Delete-Event"),
    path('Delete-Gallery/<int:id>', views.delete_gallery, name="Delete-Gallery"),
    path('Delete-Job/<int:id>', views.delete_job, name="Delete-Job"),
    path('Admin-View-Profile/<int:id>', views.Admin_View_Profile, name="Viewprofile"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
