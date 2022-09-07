from django.urls import path
from .views import HomeView, SignUpView, ShoesView, ShoeDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('shoes/', ShoesView.as_view(), name='shoes_list'),
    path('shoes/<int:pk>/', ShoeDetailView.as_view(), name='shoe_detail'),


]
