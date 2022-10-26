from django.urls import path
from .import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('postpage/<str:pk>/', views.postPage, name="postpage"),
    path('deletecomment/', views.ddeleteComment, name='delete-comment' )
    
]