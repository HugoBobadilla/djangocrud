from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.

# Add Contact
def crate_contact(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('/')
      except:
        pass
  else:
    form = ContactForm()
  
  return render(request, 'create.html', {'form': form})


def retrieve_contact(request):
  contacts = Contact.objects.all()
  return render(request, 'index.html', {'contacts': contacts})


def update_contact(request, pk):
  contacts = Contact.objects.get(contactId=pk)
  form = ContactForm(instance=contacts)

  if request.method == 'POST':
    form = ContactForm(request.POST, instance=contacts)
    if form.is_valid():
      form.save()
      return redirect('/')

  context = {
    'contacts': contacts,
    'form': form
  }

  return render(request, 'update.html', context)


def delete_contact(request, pk):
  contact = Contact.objects.get(contactId=pk)

  if request.method == "POST":
    contact.delete()
    return redirect('/')

  context = {
    'contact': contact
  }

  return render(request, 'remove.html', context)
