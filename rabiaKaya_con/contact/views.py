from django.shortcuts import render
from . forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(request.POST["konu"],request.POST["isim"],request.POST["eposta"],request.POST["mesaj"])
            messages.add_message(request, messages.SUCCESS, 'Mesajınız gönderilmiştir.')
            form = ContactForm()
        return render(request, 'iletisim.html', {'contact_form': form})
    else:
        form = ContactForm()
    return render(request, 'iletisim.html', {'contact_form': form})