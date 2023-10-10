from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_transaction),
    # path('remove/', views.remove_transaction),
    path('list/', views.get_transactions_list),
    path('balance/', views.get_balance),
]