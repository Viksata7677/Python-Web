from django.urls import path, include
from templatesAdvanced.posts.views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/', include([path('delete-post/', delete_post, name='delete-post'),
                               path('details-post/', details_page, name='details-post'),
                               path('edit_post/', edit_post, name='edit-post'),])),
]