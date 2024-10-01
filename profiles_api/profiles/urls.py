from django.urls import path,include
from profiles import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viweset')


urlpatterns = [
    path('hello-view',views.HelloApiView.as_view()),
    path('',include(router.urls))
]