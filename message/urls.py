from django.conf.urls import url
from .views import message_list


urlpatterns = [
    url(r'^list/',message_list),
]

