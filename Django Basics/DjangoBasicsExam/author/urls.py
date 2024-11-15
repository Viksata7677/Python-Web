from django.urls import path
from . import views
from .views import ProfileDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('author/create/', views.create_author, name='create_author'),
    path('author/details/', ProfileDetailView.as_view(), name='author_details'),
    path('author/edit/', views.edit_author, name='edit_author'),
    path('author/delete/', views.delete_author, name='delete_author'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
