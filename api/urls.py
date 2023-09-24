from django.urls import path

from .views import LessonViewSet, ProductViewSet, StatisticsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'product', ProductViewSet)

urlpatterns = [
    path('statistics', StatisticsView.as_view()),
    path('my_lessons', LessonViewSet.as_view({'get': 'list'}))
]

urlpatterns += router.urls
