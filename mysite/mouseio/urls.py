from django.urls import path

from . import views

app_name = "mouseio"
urlpatterns = [
    path('export', views.export_exhibits_csv, name='export_exhibits_csv'),  
    # ex: /mouseio/EN
    path("lang=<str:lang>", views.index, name="index"),
    # ex: /mouseio/about/EN
    path("about/lang=<str:lang>", views.about, name="about"),
    # ex: /mouseio/SOUTH/GR
    path("<str:location_name>/lang=<str:lang>", views.location, name="location"),
    # ex: /mouseio/MDD RF-4E Phantom II (69-7487)/EN
    path("desc/plane=<str:plane_name>/lang=<str:lang>", views.description, name="description"),
]