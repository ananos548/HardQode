from django.urls import path

from .views import LessonViewSet, ProductViewSet, StatisticsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'lessons', LessonViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('statistics', StatisticsView.as_view())
]

urlpatterns += router.urls
