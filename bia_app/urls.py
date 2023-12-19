from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, process_video


router = DefaultRouter()
router.register(r'movies', MovieViewSet)


urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('process-video/', process_video, name='process_video'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

]

urlpatterns += router.urls

