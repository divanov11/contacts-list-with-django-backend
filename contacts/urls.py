from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('deletecont/<str:pk>', views.deletecont, name='deletecont'),
    path('update', views.update, name='update'),
    path('profile/<str:pk>', views.profile, name='profile')
]