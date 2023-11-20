from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Profile


def index(request):
    """
    Display all :model:`profiles.Profile`.

    **Context**

    ``Profile``
        all instances of :model:`profiles.Profile`.

    **Template:**

    :template: `profiles\index.html`

    """

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display all :model:`profiles.Profile`.

    **Context**

    ``Profile``
        all instances of :model:`profiles.Profile`.

    **Template:**

    :template: `profiles\profile.html`

    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)

    except Profile.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
