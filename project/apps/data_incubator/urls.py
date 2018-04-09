from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from project.apps.data_incubator import views
from django.contrib.auth.decorators import login_required

urlpatterns = (
    path('upload_image/', views.UploadImageView.as_view(), name='upload_image'),
)
