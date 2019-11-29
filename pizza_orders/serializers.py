from rest_framework import serializers
from pizza_orders.models import Customer, Order, OrderItems

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderItemsCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'
        extra_kwargs = {
            'id': {
                'read_only': False, 
                'required': True
             }
        } 

class OrderUpdateSerializer(serializers.ModelSerializer):
    order_items = OrderItemsCustomSerializer(many=True, required=False)

    class Meta:
        model = Order
        exclude = ['updated', 'created']

    def update(self, instance, validated_data):
        if instance.order_status == 'Delivered':
            raise serializers.ValidationError({"order_status": "Order is already delivered, cannot update"})
        
        updated_order_items = validated_data.pop('order_items', [])
          
        item_ids = [item.get('id') for item in updated_order_items]
        print(item_ids)
        for id in item_ids:
            try:
                OrderItems.objects.get(pk=id, order=instance.pk)
            except:
                raise serializers.ValidationError({"order_items": "Item id {} not found for this order".format(id)})


        for item_data in updated_order_items:
            id = item_data.get('id')
            order_item_obj = OrderItems.objects.filter(pk=id).first()
                
            if order_item_obj:
                order_item_obj.pizza_flavour = item_data.get('pizza_flavour', order_item_obj.pizza_flavour)
                order_item_obj.quantity = item_data.get('quantity', order_item_obj.quantity)
                order_item_obj.pizza_size = item_data.get('pizza_size', order_item_obj.pizza_size)

            order_item_obj.save()

        return super(OrderUpdateSerializer, self).update(instance, validated_data)

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(many=True, required=True)

    class Meta:
        model = Order
        exclude = ['updated', 'created']

    def create(self, validated_data):
    
        customer_order_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        for data in customer_order_data:
            OrderItems.objects.create(order=order, **data)
        return order
