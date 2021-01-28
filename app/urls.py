from rest_framework import routers

from app.api import TitleApiViewSet, CountryViewSet, CategoryViewSet

router = routers.SimpleRouter(trailing_slash=True)

urlpatterns = []
router.register('title', TitleApiViewSet, basename='titles')
router.register('country', CountryViewSet, basename='countries')
router.register('category', CategoryViewSet, basename='categories')
urlpatterns += router.urls

