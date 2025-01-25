from django.urls import path
from .views import contactus, AboutUsView, AgentsView , HomeView , GoogleView



app_name = "root"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", contactus, name="contact"),
    path("about", AboutUsView.as_view(), name="about"),
    path("agent", AgentsView.as_view() , name="agent"),
    path("google", GoogleView.as_view() , name="google"),
]
