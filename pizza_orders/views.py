from rest_framework import generics
from rest_framework import viewsets
from pizza_orders.models import Order, OrderItems, Customer
from pizza_orders.serializers import OrderItemsSerializer, OrderSerializer, CustomerSerializer, OrderUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class OrderItemViewset(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order', 'pizza_flavour', 'pizza_size', 'quantity']



class OrderViewset(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    
    action_serializers = {
        'update': OrderUpdateSerializer,
        'default': OrderSerializer
    }
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer', 'order_status']

    def get_serializer_class(self):
        print (self.action)
        try:
            return self.action_serializers[self.action]
        except:
            return self.action_serializers['default']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
