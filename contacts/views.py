from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    search_input = ''
    if request.method == 'POST':
        search_input = request.POST['search-area']
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})

def new(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        relationship = request.POST['relationship']
        phonenumber = request.POST['phone-number']
        email = request.POST['e-mail']
        address = request.POST['address']
        birthday = request.POST['birthday']

        new_contact = Contact(
            full_name=fullname,
            relationship=relationship,
            email=email,
            phone_number=phonenumber,
            address=address,
            birthday=birthday)
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')

def edit(request, pk):
    pk = pk
    get_contact = Contact.objects.get(id=pk)
    return render(request, 'edit.html', {'contact': get_contact})

def update(request):
    fullname = request.POST['fullname']
    relationship = request.POST['relationship']
    phonenumber = request.POST['phone-number']
    email = request.POST['e-mail']
    address = request.POST['address']
    birthday = request.POST['birthday']
    id_no = request.POST['id']

    a = Contact.objects.get(id=id_no)
    a.full_name = fullname
    a.relationship = relationship
    a.email = email
    a.phone_number = phonenumber
    a.address = address
    a.birthday = birthday
    a.save()

    return redirect('/profile/'+id_no)

def delete(request, pk):
    pk = pk
    get_contact = Contact.objects.get(id=pk)
    return render(request, 'delete.html', {'contact': get_contact})
    
def deletecont(request, pk):
    pk = pk
    get_contact = Contact.objects.get(id=pk)
    get_contact.delete()
    return redirect('/')

def profile(request, pk):
    pk = pk
    get_contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': get_contact})