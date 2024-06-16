from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Product, Bids

# Create your views here.
def index(request):
    current_time = timezone.now()
    products = Product.objects.filter(ending_date__gt=current_time)
    return render(request, "core/index.html", {'products': products})

def addBid(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        highest_bid = Bids.objects.filter(product=product).order_by('-amount').first()

        if not product_id or not amount:
            return HttpResponse("Invalid data.", status=400)

        try:
            amount = float(amount)
        except ValueError:
            return HttpResponse("Invalid bid amount.", status=400)

        if amount < product.starting_bid:
            return HttpResponse("Your bid must be higher than the starting bid.", status=400)
        
        if highest_bid and amount <= highest_bid.amount:
            return HttpResponse("Your bid must be higher than the current highest bid.", status=400)

        if timezone.now() > product.ending_date:
            return HttpResponse("The auction has ended.", status=400)


        new_bid  = Bids(
            user = request.user.id,
            product = product,
            amount = request.POST.get('amount'),
        )

        new_bid.save()
        return redirect('index', request)
    else:
         return render(request, 'core/index.html')

def removeBid(request):
    pass

def changeBid(request):
    pass

def showBids(request):
    pass

def addProduct(request):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    if request.method == 'POST':
        try:
            new_product = Product(
                product_name = request.POST.get('product_name'),
                product_image = request.POST.get('product_url'),
                starting_bid = int(request.POST.get('starting_bid')),
                author = request.user
            )
            new_product.save()
            return render(request, 'core.index.html')
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)
    else:
        return render(request, 'core/add_product.html')

def removeProduct(request):
    pass