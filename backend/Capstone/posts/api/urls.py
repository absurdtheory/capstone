from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.api import views as pv

router = DefaultRouter()
router.register(r"posts", pv.PostViewSet) # Posts endpoint

urlpatterns = [
    path("", include(router.urls)),
]
