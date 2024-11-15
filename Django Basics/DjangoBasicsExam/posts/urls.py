from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('<int:id>/details/', post_details, name='post_details'),
    path('<int:id>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='delete_post'),
]
