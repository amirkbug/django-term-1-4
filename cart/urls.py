from django.urls import path
from .views import cart_view, CheckoutView

app_name = "cart"
urlpatterns = [
    path("", cart_view, name="cart_view"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
