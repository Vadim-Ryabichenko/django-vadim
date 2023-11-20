from .views import profile_page, set_password_page, set_userdata_page, deactivate_account_page, register_account_page, login_page, logout_page
from django.urls import path


urlpatterns = [
    path('profile/<str:username>/', profile_page),
    path('set-password/', set_password_page),
    path('set-userdata/', set_userdata_page),
    path('deactivate/', deactivate_account_page),
    path('register/', register_account_page, name = "register_page"),
    path('login/', login_page, name = "login_page"),
    path('logout/', logout_page, name = "logout_page"),
]