from django.urls import path
from .views import perfilview

urlpatterns = [
       path("",perfilview.as_view(), name='curriculum'),
]