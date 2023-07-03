from django.urls import path,include

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('activities/', views.activity_listing, name='activities'),
    path('activities/fetch-more/', views.fetch_more_activities, name='fetch_more_activities'),
    path('edit/<int:activity_id>/', views.edit_activity, name='edit_activity'),
]