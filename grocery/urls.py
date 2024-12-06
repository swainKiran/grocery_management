from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('print-bill/', views.print_bill, name='print_bill'),
    path('delete-all/', views.delete_all_transactions, name='delete_all_transactions'),

]