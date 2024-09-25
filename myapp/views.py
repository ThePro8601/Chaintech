from django.shortcuts import render
from datetime import datetime
import random
from django.http import HttpResponse
from .models import Contact

def home(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    quotes = [
        "To be or not to be, that is the question.",
        "The only thing we have to fear is fear itself.",
        "I think, therefore I am.",
        "Courage is being scared to death, but saddling up anyway.",
        "Well done is better than well said.",
        "The way to get started is to quit talking and begin doing",
        "Keep calm and carry on."
    ]
    random_quote = random.choice(quotes)
    context = {
        'current_time': current_time,
        'random_quote': random_quote
    }
    return render(request, 'index.html', context)

def handle_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email)
        contact.save()
        return HttpResponse(f"Thank you {name}! We have received your email: {email}.")
    return HttpResponse("Invalid request.")

def view_data(request):
    contacts = Contact.objects.all()
    return render(request, 'view_data.html', {'contacts': contacts})

