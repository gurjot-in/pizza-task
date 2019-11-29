from django.urls import path
from pizza_orders import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'customers', views.CustomerViewSet, base_name= 'customers')
router.register(r'orders', views.OrderViewset, base_name = 'orders')
router.register(r'order_items', views.OrderItemViewset, base_name = 'order_items')
urlpatterns = router.urls