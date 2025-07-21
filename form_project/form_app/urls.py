from django.contrib import admin
from django.urls import path
from form_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.submit_form, name='submit_form'),
    path('success/', views.success_view, name='success'),
]
