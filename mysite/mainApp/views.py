from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/contact.html', {'values': ['number: (029)456-76-97', "e-mail: new_weather@mail.com"]})
