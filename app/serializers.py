from rest_framework import serializers
from app.models import Client, Order, Deliver


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'orderDetails': {
                'name': instance.name,
                'type': instance.type,
                'size': instance.size,
                'amount': instance.amount,
                'address': instance.address,
                'registeredDateTime': instance.registered,
                'updatedDateTime': instance.updated,
            },
            'clientDetails': {
                'firstname': instance.client.firstname,
                'lastname': instance.client.lastname,
                'email': instance.client.email,
                'phoneNumber': instance.client.phone_number,
                'registeredDateTime': instance.client.registered,
                'updatedDateTime': instance.client.updated,
            },
            'deliverDetails': {
                'firstname': instance.deliver.firstname,
                'lastname': instance.deliver.lastname,
                'authKey': instance.deliver.auth_key,
                'registeredDateTime': instance.deliver.registered,
                'updatedDateTime': instance.deliver.updated,
            },
            'status': {
                'orderStatus': instance.status,
            },
        }


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = '__all__'
