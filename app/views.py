from app.models import Order, Deliver, Client
from app.serializers import OrderSerializer, DeliverSerializer, ClientSerializer
from rest_framework import generics


# ORDER VIEWS
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# DELIVER VIEWS
class DeliverList(generics.ListCreateAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer


class DeliverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer


# CLIENT VIEWS
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
