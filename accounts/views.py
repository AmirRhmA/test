from django.views.generic import ListView, DetailView, CreateView
from .models import Shoe
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class HomeView(ListView):
    template_name='home.html'
    model = Shoe

class ShoesView(ListView):
    template_name='shoes.html'
    model = Shoe

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ShoeDetailView(DetailView):
    template_name='shoes_detail.html'
    model = Shoe