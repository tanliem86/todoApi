
from django.urls import path,include
from rest_framework import routers
from .views import TodoView

router= routers.DefaultRouter()
router.register('todo',TodoView,basename='todos')
urlpatterns = [

    path('',include(router.urls))
]
