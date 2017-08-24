from django.conf.urls import url
from .views import activate


urlpatterns = [
    url(r'^(?P<code>\w+)$',activate),
]
