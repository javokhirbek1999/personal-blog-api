from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AllUsers, BlacklistTokenUpdateView

app_name = 'users'

router = DefaultRouter()
router.register('', AllUsers)


urlpatterns = [
    path('',include(router.urls)),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]