from django.urls import path

from . import views

app_name = "mouseio"
urlpatterns = [
    # ex: /mouseio/
    path("", views.index, name="index"),
    # ex: /mouseio/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /mouseio/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /mouseio/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
]