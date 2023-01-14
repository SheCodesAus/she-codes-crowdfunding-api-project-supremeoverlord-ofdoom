from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"), #need to have / after projects because we are not psychopaths and "name=project-list" is django standard
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail"),
    path('pledges/', views.PledgeList.as_view(), name="pledge-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns) #takes all your urls and lets you choose if you want json ect back - low value in reality

