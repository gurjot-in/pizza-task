from django.urls import path
from pizza_orders import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewset)
router.register(r'order_items', views.OrderItemViewset)
urlpatterns = router.urls