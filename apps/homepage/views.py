from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.announcements.forms import AnnouncementForm
from apps.announcements.models import Announcements
from apps.authentication.models import Departments, User
from apps.extension.forms import ExtensionForm
from apps.extension.models import Extension
from apps.homepage.forms import DepartmentForm
from apps.researches.forms import ResearchForm
from apps.researches.models import Research
from apps.subjects.forms import SubjectsForm
from apps.subjects.models import Subjects


@login_required(login_url='/signin')
def index(request):
    template_name = "layout.html"

    # Querysets
    published_announcements = Announcements.objects.filter(status="published")
    faculty_subjects = Subjects.objects.filter(faculty_subjects__user=request.user)
    researches = Research.objects.filter(posted_by=request.user)
    extensions = Extension.objects.filter(posted_by=request.user)
    department = Departments.objects.filter(created_by=request.user)
    faculty = User.objects.filter(is_faculty=True)
    all_researches = Research.objects.all()

    # forms
    subjects_form = SubjectsForm(user=request.user)
    research_form = ResearchForm(request.POST or None, request.FILES or None)
    extension_form = ExtensionForm(request.POST or None, request.FILES or None)
    dept_form = DepartmentForm(request.POST or None)
    announcement_form = AnnouncementForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        name = request.POST.get('announcement_form')
        print(name)
        if request.POST.get('extension_form'):
            if extension_form.is_valid():
                form = extension_form.save(commit=False)
                form.posted_by = request.user
                form.save()
                return redirect("/")

        elif request.POST.get('announcement_form'):
            if announcement_form.is_valid():
                form = announcement_form.save(commit=False)
                form.posted_by = request.user
                form.save()
                return redirect("/")

        else:
            if dept_form.is_valid():
                form = dept_form.save(commit=False)
                form.created_by = request.user
                form.save()
                return redirect("/")


    context = {
        "published_announcements": published_announcements,
        "faculty_subjects": faculty_subjects,
        "subjects_form": subjects_form,
        "researches": researches,
        "research_form": research_form,
        "extensions": extensions,
        "extension_form": extension_form,
        "department": department,
        "dept_form": dept_form,
        "faculty": faculty,
        "announcement_form": announcement_form,
        "all_researches": all_researches
    }

    return render(request, template_name, context)


def delete_department(request, id):
    obj = Departments.objects.get(id=id)
    obj.delete()
    return redirect("/")
