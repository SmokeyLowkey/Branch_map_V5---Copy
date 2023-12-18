"""branchwatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView

from django.conf.urls import url
import django.contrib.auth.views

import branchwatchapp.views  # Import views from your app
import branchwatchapp.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(url='admin/'), name='home'),  # Redirect to admin login
    path('admin/', admin.site.urls),
    path('map/', branchwatchapp.views.home, name='map_page'),
    path('tinymce/', include('tinymce.urls')),
    path('companybranch_dataset/', branchwatchapp.views.companybranch_dataset, name='companybranch_dataset'),
    path('get_branch_info/<str:branch_id>/', branchwatchapp.views.get_branch_info, name='get_branch_info'),
    path('get_branch_contact/<str:branch_id>/', branchwatchapp.views.get_branch_contact, name='get_branch_contact'),
    # path('your_url/', branchwatchapp.views.your_view_function, name='your_view_name'),
    path('get_branch_headers/', branchwatchapp.views.get_branch_headers, name='get_branch_headers'),
    path('division_dataset/<str:division>/', branchwatchapp.views.division_dataset, name='division_dataset'),
    # path('login/', auth_views.LoginView.as_view(template_name='\app\registration\login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('division_dataset/CF/', branchwatchapp.views.cf_division_dataset, name='cf_division_dataset'),
    # path('division_dataset/TT/', branchwatchapp.views.tt_division_dataset, name='tt_division_dataset'),
    # Add other routes here...
]


