from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('users/', views.users_view, name='users'),
    path('roles/', views.roles_view, name='roles'),
    path('permissions/', views.permissions_view, name='permissions'),
]


urlpatterns += [
    path('add-role/', views.add_role, name='add_role'),
    path('delete-role/<int:role_id>/', views.delete_role, name='delete_role'),
    path('update-permission/<int:role_id>/', views.update_permission, name='update_permission'),


    path('add_user/', views.add_user, name='add_user'),  # Add this line
    path('edit_user/', views.edit_user, name='edit_user'),  # For editing
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    path('roles/', views.roles_view, name='roles'),
    path('roles/add/', views.add_role, name='add_role'),
    path('roles/edit/<int:role_id>/', views.edit_role, name='edit_role'),
    path('roles/delete/<int:role_id>/', views.delete_role, name='delete_role')
]


