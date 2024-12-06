

from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem, GroceryTransaction
from .forms import GroceryTransactionForm
from decimal import Decimal
def home(request):
    transactions = GroceryTransaction.objects.all()
    total_price = sum(transaction.total_price for transaction in transactions)
    return render(request, 'grocery/home.html', {
        'transactions': transactions,
        'total_price': total_price
    })

def add_item(request):
    if request.method == "POST":
        item_id = request.POST['item']
        kg_quantity = Decimal(request.POST.get('kg_quantity', 0))  # Default to 0 if not provided
        gm_quantity = Decimal(request.POST.get('gm_quantity', 0))  # Default to 0 if not provided

        # Combine kilograms and grams into a single quantity in kilograms
        total_quantity = kg_quantity + (gm_quantity / Decimal(1000))

        # Get the selected item
        item = get_object_or_404(GroceryItem, id=item_id)

        # Create the transaction
        transaction = GroceryTransaction(
            item=item,
            quantity=total_quantity
        )
        transaction.save()  # This will calculate the total price automatically
        return redirect('home')

    # For GET requests
    query = request.GET.get('search', '')
    items = GroceryItem.objects.filter(name__icontains=query) if query else GroceryItem.objects.all()
    return render(request, 'grocery/add_item.html', {'items': items, 'query': query})
def edit_item(request, pk):
    item = GroceryItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = GroceryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GroceryItemForm(instance=item)
    return render(request, 'grocery/edit_item.html', {'form': form})
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(GroceryTransaction, id=transaction_id)
    transaction.delete()
    return redirect('home')

def print_bill(request):
    transactions = GroceryTransaction.objects.all()
    total_price = sum(transaction.total_price for transaction in transactions)
    return render(request, 'grocery/print_bill.html', {'transactions': transactions, 'total_price': total_price})

def delete_all_transactions(request):
    GroceryTransaction.objects.all().delete()
    return redirect('home')

# def add_item(request):
#     query = request.GET.get('search', '')  # Get the search query from the request
#     items = GroceryItem.objects.filter(name__icontains=query) if query else GroceryItem.objects.all()
    
#     if request.method == 'POST':
#         item_id = request.POST.get('item')
#         quantity = int(request.POST.get('quantity'))
#         item = GroceryItem.objects.get(id=item_id)
#         total_price = item.price_per_unit * quantity

#         # Save transaction
#         GroceryTransaction.objects.create(item=item, quantity=quantity, total_price=total_price)
#         return redirect('home')

#     return render(request, 'grocery/add_item.html', {'items': items, 'query': query})
