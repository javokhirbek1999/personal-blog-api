from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AllUsers, SuperuserView, BlacklistTokenUpdateView

app_name = 'users'

router = DefaultRouter()
router.register('users', AllUsers)
router.register('superusers',SuperuserView)


urlpatterns = [
    path('',include(router.urls)),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]