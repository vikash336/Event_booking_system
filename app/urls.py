from . import views
from django.urls import path
from .views import CR , UserLoginView , send_email_to_all

urlpatterns = [
    path("test/", CR.as_view() ),
    path("login/", UserLoginView.as_view() ),
    path("email/", views.send_email_to_all, name="test")

]
