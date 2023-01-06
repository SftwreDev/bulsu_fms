from django.shortcuts import render, redirect

from apps.authentication.models import Actor


# Create your views here.

def faculty_add_subjs(request):
    if request.method == "POST":
        subjs = request.POST.getlist("subjects")
        actor = Actor.objects.filter(user_id=request.user.id)

        for subj in subjs:
            for user in actor:
                user.subjects.add(subj)
        return redirect("/")


def remove_faculty_subjs(request, id):
    faculty = Actor.objects.filter(user=request.user)

    for user in faculty:
        user.subjects.remove(id)
    return redirect("/")
