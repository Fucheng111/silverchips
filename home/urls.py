"""News home URL Configuration.

Included directly under the root of the site.
"""

# Django imports
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

# Local imports
from . import views

# Custom URL patterns
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^story/([0-9]+)$", views.read_story, name="read_story"),
    url(r"^image/([0-9]+)$", views.view_image, name="view_image")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)