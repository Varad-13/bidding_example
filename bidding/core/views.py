from django.shortcuts import render
from .models import Product, Bids

# Create your views here.
def index(request):
    return render(request, "core/index.html")

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
        return redirect('index')
    else:
         return HttpResponse("Invalid request method.", status=405)

def removeBid(request):
    pass

def changeBid(request):
    pass

def showBids(request):
    pass

def addProduct(request):
    pass

def removeProduct(request):
    pass