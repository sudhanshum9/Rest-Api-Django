from django.urls import path
from profile_api import views


urlpatterns = [
    path('hello-api-view/',views.HelloApiView.as_view()),
]