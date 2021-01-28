from django.conf.urls import url
from rest_framework import routers

from app.api import TitleApiViewSet

router = routers.SimpleRouter(trailing_slash=True)

urlpatterns = []
router.register('', TitleApiViewSet, basename='titles')
urlpatterns += router.urls

