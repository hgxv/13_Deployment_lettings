from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
    Display all :model:`lettings.Letting`.

    **Context**

    ``Letting``
        all instances of :model: `lettings.Letting`.

    **Template:**

    :template: `lettings/index.html`

    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Display an individual :model:`lettings.Letting`.

    **Context**

    ``Letting``
        An instance of :model: `lettings.Letting`.

    **Template:**

    :template: `lettings/letting.html`

    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
