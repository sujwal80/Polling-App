from django.urls import path
from .views import home, vote, result, register, signout
from django.contrib.auth import views

urlpatterns = [
    path('', home, name="home_page"),
    path('poll/<pk>', vote, name="voting_page"),
    path('poll/results/<pk>', result, name="result_page"),
    path('account/signup', register, name="register_page"),
    path('account/signin', views.LoginView.as_view(template_name="login.html"), name="login_page"),
    path('account/signout', signout, name="logout_page")
]