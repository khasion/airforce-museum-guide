from django.urls import path

from . import views

app_name = "mouseio"
urlpatterns = [
    # ex: /export
    path('export', views.export_exhibits_csv, name='export_exhibits_csv'),  
    # ex: /
    path("", views.index, name="index"),
    # ex: /lang=en
    path("lang=<str:lang>", views.index, name="index"),
    # ex: /contact/lang=en
    path("contact/lang=<str:lang>", views.contact, name="contact"),
    # ex: /SOUTH/lang=el
    path("<str:location_name>/lang=<str:lang>", views.location, name="location"),
    # ex: desc/plane=MDD RF-4E Phantom II (69-7487)/lang=en
    path("desc/plane=<int:plane_id>/lang=<str:lang>", views.description, name="description"),
]