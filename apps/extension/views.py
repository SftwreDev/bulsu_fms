from django.shortcuts import render, redirect

from apps.authentication.models import User
from apps.extension.models import Extension


# Create your views here.
def extension_detail(request, slug):
    template_name = "extension_detail.html"

    obj = Extension.objects.get(slug=slug)
    context = {
        "extension": obj
    }
    return render(request, template_name, context)


def extension_delete(request, slug):

    obj = Extension.objects.get(slug=slug)
    obj.delete()
    return redirect("/")


def filter_extension(request):
    template_name = "research_filter_results.html"
    filter = request.GET.get("filter_research")
    users = User.objects.all()
    if filter == "with_research":
        for user in users:
            publisher = Extension.objects.filter(posted_by__id=user.id)
            context = {
                'publisher': publisher
            }
            return render(request, template_name, context)
    elif filter == "without_research":
        for user in users:
            publisher = User.objects.filter(research_publisher__isnull=True).distinct()
            context = {
                'publisher': publisher
            }
            return render(request, template_name, context)
            return render(request, template_name, context)