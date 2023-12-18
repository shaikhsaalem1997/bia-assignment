from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, process_video


router = DefaultRouter()
router.register(r'movies', MovieViewSet)


urlpatterns = [
    path('hello/', views.hello_django, name='hello'),
    path('process-video/', process_video, name='process_video'),
]

urlpatterns += router.urls

