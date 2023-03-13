from django.urls import path

from . import views
from .views import ChangePasswordView

urlpatterns = [
    path('', views.CustomUserList.as_view(), name ='customuser-list'), #if we don't get any information then handle it this way
    path('<int:pk>', views.CustomUserDetail.as_view(), name='customuser-detail'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]