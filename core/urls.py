from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('uavs.html', views.uavs, name='uavs'),
    path('about.html', views.about, name='about'),
    path('uavs/<int:uav_id>/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('login.html', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register.html', views.register_user, name='register'),
    path('edit_profile.html', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('add/', views.add_uav, name='add_uav'),
    path('delete/<int:uav_id>/', views.delete_uav, name='delete_uav'),
    path('update/<int:uav_id>/', views.update_uav, name='update_uav'),
    path('list/', views.list_uavs, name='list_uavs'),
    path('rent_uav.html', views.rent_uav, name='rent_uav'),
    path('rentals/', views.rental_list, name='rental_list'),
    path('rentals/<int:pk>/update/', views.rental_update, name='rental_update'),
    path('rentals/<int:pk>/delete/', views.rental_delete, name='rental_delete'),
    path('uav/<int:pk>/delete_lease/<int:lease_id>/', views.delete_lease, name='delete_lease'),
    path('uav/<int:pk>/update_lease/<int:lease_id>/', views.update_lease, name='update_lease'),
    path('uav/<int:pk>/list_leases/', views.list_leases, name='list_leases'),
]
