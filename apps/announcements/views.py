from django.shortcuts import render

from apps.announcements.models import Announcements


# Create your views here.
def announcements_detail(request, slug):
    template_name = "announcement_detail.html"

    obj = Announcements.objects.get(slug=slug)
    context = {
        "announcements": obj
    }
    return render(request, template_name, context)