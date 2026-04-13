from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("heart/", views.heart, name="heart"),
    path("diabetes/", views.diabetes, name="diabetes"),
    path("stress/", views.stress, name="stress"),
    path("live-ai/", views.live_ai, name="live_ai"),
    path("live-ai/message/", views.live_ai_message, name="live_ai_message"),
]