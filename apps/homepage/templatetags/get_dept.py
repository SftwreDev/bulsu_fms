from django import template

from apps.authentication.models import Departments

register = template.Library()


@register.filter
def get_dept(value):
    dept = Departments.objects.get(id=value)
    return dept.department
