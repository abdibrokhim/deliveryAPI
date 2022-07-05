from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    # Client View List
    path('client/', views.ClientList.as_view()),
    path('client/<int:pk>/', views.ClientDetail.as_view()),

    # Order View List
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),

    # Deliver View List
    path('deliver/', views.DeliverList.as_view()),
    path('deliver/<int:pk>/', views.DeliverDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
