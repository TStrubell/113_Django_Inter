from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Create your views here.
# Function-based view 

# Class Based Views
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        return context

# Function Based Views
def home_page(request):
    # return HttpResponse("Hello World from FBV")
    return render(request, 'pages/home.html', {'title': 'Home Page'})

def about_page(request):
    return render(request, 'pages/about.html', {'title': 'About Us'})

def contact_page(request):
    return render(request, 'pages/contact.html', {'title': 'Contact Us'})