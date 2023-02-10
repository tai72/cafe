from django.urls import path
from . import views

app_name = 'cafe_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"), 
    path('menu', views.MenuView.as_view(), name="menu"), 
    path('contact', views.ContactView.as_view(), name="contact"), 
    path('original-menu-list', views.OriginalMenuList.as_view(), name="original_menu_list"), 
]
