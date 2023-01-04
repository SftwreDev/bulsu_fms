from django.shortcuts import render, redirect

from apps.authentication.models import User
from apps.researches.models import Research


# Create your views here.
def add_research(request):
    if request.method == "POST":
        print(request.POST)
        document = request.FILES.get('document')
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        status = request.POST.get('status')

        Research.objects.create(
            document=document,
            title=title,
            summary=summary,
            status=status,
            posted_by=request.user
        )

        return redirect("/")


def delete_research(request, id):
    obj = Research.objects.filter(id=id)
    obj.delete()
    return redirect("/")


def filter_research(request):
    template_name = "research_filter_results.html"
    filter = request.GET.get("filter_research")
    users = User.objects.all()
    if filter == "with_research":
        for user in users:
            publisher = Research.objects.filter(posted_by__id=user.id)
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
