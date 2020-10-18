from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

from django.shortcuts import render
from .models import fichas



def index(request):
    
    ficha = fichas.objects.all()    
    dados={'fichas': ficha}

    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return render(request,'index.html', dados)



def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "urlTeste", #request.build_absolute_uri(reverse('paypal-ipn')),
        "return": "urlTeste", #request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": "urlTeste", #request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "paypal.html", context)
