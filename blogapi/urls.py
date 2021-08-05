from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


app_name = 'posts'

router = DefaultRouter()
router.register('', views.PostList, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('comments/<str:pk>/', views.Comments.as_view(), name='comments'),
    path('comments/replies/<str:pk>/', views.Replies.as_view(), name='replies'),
]