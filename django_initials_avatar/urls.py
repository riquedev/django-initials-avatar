from django.urls import path
from .views import SVGInitialsAvatarView

urlpatterns = [
    path('svg', SVGInitialsAvatarView.as_view(), name="initials-avatar-svg")
]
