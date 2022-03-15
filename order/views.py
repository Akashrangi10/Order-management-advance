from decimal import Decimal
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Order,Customer,Product
from .forms import OrderForm
# Create your views here.

# Listing Orders
def index_view(request):
    orders = Order.objects.values('id','customer_id__first_name','product_id__name','unit_price','qty','total_price')
    context = {
        'orders':orders
    }
    return render (request,'order/index.html',context=context)

# Create Order
def create_order(request):
    customer = Customer.objects.values("id","first_name")
    product = Product.objects.values("id","name","unit_proce")
    
    if request.POST:
        customer = request.POST['customers']
        product = request.POST['products']
        prices = request.POST['price']
        total =request.POST['totalprice']
        Order.objects.create(customer_id_id=customer,product_id_id =product,unit_price =prices,
        qty=request.POST['quentity'],
        total_price= total
        )
        return redirect('index')
    else:
        
        return render(request,'order/create_order2.html',{'all_customer':customer,'all_product':product})




def delete_order_view(request,orders_id):
    order = Order.objects.get(pk=orders_id)
    
    order.delete()
    return redirect('index')
    


# Update order

def update_order(request,order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.qty= request.POST['quentity']
        order.total_price = request.POST['totalprice']
        order.save()
        return redirect('index')
    else:
        return render(request,'order/update_order.html',{'order':order})