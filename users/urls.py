from django.urls import path

from users.views import users

urlpatterns = [
    path('users/reg/', users.RegistrationView.as_view(), name='reg')
]