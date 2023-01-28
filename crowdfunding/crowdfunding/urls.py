"""crowdfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
    path("", include('projects.urls')), #we will pass everything through here
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]

#can't get it into json format, blanket 404 error page for everything thats not handled in views
# def blanket_404_response(request, exception):
#         return HttpResponseNotFound("404 Error, It seems you have traveled to a nonexistent place. A gnome has gifted you one GnomeBuck to take with you on your journey. (*GnomeBucks have no monetary value)")


def blanket_404_response(request, exception):
        return JsonResponse({
            'status_code': 404,
            'error': "404 Error, It seems you have traveled to a nonexistent place. A gnome has gifted you one GnomeBuck to take with you on your journey. (*GnomeBucks have no monetary value)"
        })

handler404 = blanket_404_response
