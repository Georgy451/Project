from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from .views import TrackView

urlpatterns = [
    path('', index, name='home'),
    path('base', base, name='base'),
    path('profile', profile, name='profile'),
    path('about', about, name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('track/', TrackView.as_view(), name='track'),
    path('user', user, name='user'),
    path('subscribe/<int:user_id>/', subscribe, name='subscribe'),
    path('unsubscribe/<int:user_id>/', unsubscribe, name='unsubscribe'),
    path('user/<int:user_id>/', user_profile, name='user_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)