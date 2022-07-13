from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_reroute),
    path('amadon', views.amadon),
    path('purchase/<int:product_id>', views.process_purchase),
    path('amadon/checkout', views.success)
]