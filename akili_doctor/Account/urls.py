from django.urls import path
from .views import CurrentUserView, AccountDetail, LoginView, CustomRegisterView, LogoutView, DeleteAccountView

urlpatterns = [
    path('', CurrentUserView.as_view(), name='account'),
    path('<int:pk>/', AccountDetail.as_view(), name='account-detail'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete-account'),
]