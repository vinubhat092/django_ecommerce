from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="Search"),
    path('productview/',views.productview,name="Productview"),
    path('checkout/',views.checkout,name="Checkout"),
]
