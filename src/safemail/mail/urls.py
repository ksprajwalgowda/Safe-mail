from django.urls import path

from . import views

app_name = 'mail'

urlpatterns = [
    path('', views.home, name='home'),
    path('compose/', views.compose, name="compose"),
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent, name='sent'),
    path('inbox/<pk>/delete/',views.Maildelete.as_view(), name="delete"),
    # path('getin/', views.getin, name="getin"),

]