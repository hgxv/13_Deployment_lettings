from django.shortcuts import render


def index(request):
    """
    Display the index page with access buttons to apps

    **Template:**

    :template: `base.html`

    """
    return render(request, "index.html")
