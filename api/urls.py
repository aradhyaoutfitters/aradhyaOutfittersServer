from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path("api/contact", views.ContactListCreateView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
