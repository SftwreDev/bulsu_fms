from django.shortcuts import render, redirect

from apps.authentication.models import Faculty


# Create your views here.

def faculty_add_subjs(request):
    if request.method == "POST":
        subjs = request.POST.getlist("subjects")
        faculty = Faculty.objects.filter(user=request.user)

        if type(subjs) is list:
            for subj in subjs:
                for user in faculty:
                    user.subjects.add(subj)
        else:
            for user in faculty:
                user.subjects.add(subjs)
        return redirect("/")


def remove_faculty_subjs(request, id):
    faculty = Faculty.objects.filter(user=request.user)

    for user in faculty:
        user.subjects.remove(id)
    return redirect("/")