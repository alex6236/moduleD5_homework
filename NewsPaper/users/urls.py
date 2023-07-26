from django.urls import path
from .views import AccountsView, upgrade_me

app_name = 'users'
urlpatterns = [
    path('profile/', AccountsView.as_view(), name='profile'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
]