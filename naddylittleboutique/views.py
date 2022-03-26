from django.http import HttpResponse
from  django.shortcuts import render

from .validations.forms import ContactForm

def home_pageold(request):
    return HttpResponse("hello world")

def home_page(request):
    context = {
        'title':'hello World',
        'content':'Welcome to the Home Page'
    }
    return render(request, "home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title':'Contact our boutique',
        'content':'Welcome to the contact Page',
        'form' : contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST.get('email'))
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('content'))


    return render(request, "contact/view.html",context)

def about_page(request):
    context = {
        "title":"About Naddy's little Boutique",
        'content':'Welcome to the About Page'
    }


    return render(request, "home_page.html",context)