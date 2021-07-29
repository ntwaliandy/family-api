
from django import urls
from django.urls import path, include
from rest_framework import routers, urlpatterns
from .import views

router = routers.DefaultRouter()
router.register(r'families', views.FamilyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]