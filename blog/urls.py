from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.gonderiliste, name="gonderiliste"),
    path('gonderi/<int:pk>',views.gonderidetay, name="gonderidetay"),
    path('gonderi/<int:pk>/edit/',views.gonderiduzenle, name="editgonderi"),
    # path('yeni',views.yeniGonderi,name="yeniGonderi"),
    path('yeni',views.CreateGonderiView.as_view(),name="yeniGonderi"),
]
