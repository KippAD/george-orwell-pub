from django.urls import path
from .views import AccountPage, AdminPage, logout_view, contact


app_name = "myaccount"
urlpatterns = [
    path('myaccount', AccountPage.as_view(), name='account'),
    path('admin', AdminPage.as_view(), name="admin"),
    path("contact", contact, name="contact"),
    path('logout', logout_view, name="logout")
]
