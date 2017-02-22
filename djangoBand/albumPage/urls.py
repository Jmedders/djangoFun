from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from albumPage.models import Album

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Album.objects.all().order_by("band"),
    template_name = "album/album.html"))
]
