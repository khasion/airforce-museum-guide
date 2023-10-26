from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import csv
import requests


from .models import Exhibit, LocationDescription, ExhibitDescription

def index(request, lang="en"):
    locations = LocationDescription.objects.filter(lang = lang)
    context = {"location_list": locations}
    if lang == 'en':
        return render(request, "mouseio/index-en.html", context)
    if lang == 'de':
        return render(request, "mouseio/index-de.html", context)
    if lang == 'fr':
        return render(request, "mouseio/index-fr.html", context)
    if lang == 'it':
        return render(request, "mouseio/index-it.html", context)
    if lang == 'es':
        return render(request, "mouseio/index-es.html", context)
    if lang == "pl":
        return render(request, "mouseio/index-pl.html", context)
    else:
        return render(request, "mouseio/index-el.html", context)

def location(request, location_name, lang):
    location = LocationDescription.objects.filter(name = location_name, lang = lang)
    exhibits = Exhibit.objects.filter(location = location_name)
    descriptions = ExhibitDescription.objects.filter(exhibit__in = exhibits, lang = lang)

    shortened = []
    for i, _ in enumerate(descriptions):
        shortened.append(descriptions[i].text[:100] + '...')

    target = exhibits[0].pk
    exhibits_zipped = list(zip(exhibits, shortened))

    context = {'exhibits': exhibits_zipped, 'location': location, 'descriptions': descriptions, 'target': target, 'target_id': exhibits[0].pk, 'is_desc': 0}
    if lang == 'en':
        return render(request, "mouseio/location-en.html", context)
    if lang == 'de':
        return render(request, "mouseio/location-de.html", context)
    if lang == 'fr':
        return render(request, "mouseio/location-fr.html", context)
    if lang == 'it':
        return render(request, "mouseio/location-it.html", context)
    if lang == 'es':
        return render(request, "mouseio/location-es.html", context)
    if lang == "pl":
        return render(request, "mouseio/location-pl.html", context)
    else:
        return render(request, "mouseio/location-el.html", context)


def description(request, plane_id, lang):
    target_exhibit = Exhibit.objects.get(exhibit_ID = plane_id)
    location = LocationDescription.objects.filter(name = target_exhibit.location, lang = lang)
    exhibits = Exhibit.objects.filter(location = target_exhibit.location)
    descriptions = ExhibitDescription.objects.filter(exhibit__in = exhibits, lang = lang)

    shortened = []
    for i, _ in enumerate(descriptions):
        shortened.append(descriptions[i].text[:100] + '...')

    exhibits_zipped = list(zip(exhibits, shortened))

    context = {'exhibits': exhibits_zipped, 'location': location, 'descriptions': descriptions, 'target': target_exhibit.pk, 'target_id': plane_id, 'is_desc': 1}
    if lang == 'en':
        return render(request, "mouseio/location-en.html", context)
    if lang == 'de':
        return render(request, "mouseio/location-de.html", context)
    if lang == 'fr':
        return render(request, 'mouseio/location-fr.html', context)
    if lang == 'it':
        return render(request, "mouseio/location-it.html", context)
    if lang == 'es':
        return render(request, "mouseio/location-es.html", context)
    if lang == "pl":
        return render(request, "mouseio/location-pl.html", context)
    else:
        return render(request, "mouseio/location-el.html", context)

def contact(request, lang):
    if lang == 'en':
        return render(request, "mouseio/contact-en.html")
    if lang == 'de':
        return render(request, "mouseio/contact-de.html")
    if lang == 'fr':
        return render(request, "mouseio/contact-fr.html")
    if lang == 'it':
        return render(request, "mouseio/contact-it.html")
    if lang == 'es':
        return render(request, "mouseio/contact-es.html")
    if lang == "pl":
        return render(request, "mouseio/contact-pl.html")
    else:
        return render(request, "mouseio/contact-el.html")


def export_exhibits_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exhibit_descriptions.csv"'

    writer = csv.writer(response)
    writer.writerow(['exhibit', 'text', 'lang'])

    users = ExhibitDescription.objects.filter(lang = 'en').values_list('exhibit', 'text', 'lang')
    for user in users:
        writer.writerow(user)

    return response