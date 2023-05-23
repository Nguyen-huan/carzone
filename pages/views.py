from django.shortcuts import render
import os


# Create your views here.
def home(request):
    print("file tuong doi", __file__)
    print("file tuyet doi", os.path.abspath(__file__))
    print("file cha 1", os.path.dirname(os.path.abspath(__file__)))
    print("file cha 1", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    return render(request, "pages/home.html", {})


def contact(request):
    return render(request, "pages/contact.html")


def about(request):
    return render(request, "pages/about.html")


def services(request):
    return render(request, "pages/services.html")
