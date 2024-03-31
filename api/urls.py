from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, UserViewSet

router = DefaultRouter()
router.register('products-api', ProductViewSet)
router.register('category-api', CategoryViewSet)
router.register('user-api', UserViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
