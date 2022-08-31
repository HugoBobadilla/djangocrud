from django.urls import path
from . import views

urlpatterns = [
  path('', views.crate_contact, name='create-contact'),
  path('search/', views.retrieve_contact, name='retrieve-contact'),
  path('update/<int:pk>', views.update_contact, name='update-contact'),
  path('delete/<int:pk>', views.delete_contact, name='delete-contact')
]