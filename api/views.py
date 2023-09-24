from django.contrib.auth.models import User
from django.db.models import Count, Sum, F, Q, Prefetch
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Product, Lesson, LessonAccess
from .serializers import LessonSerializer, ProductSerializer
from .mixins import IsAuthenticatedMixin


class LessonViewSet(IsAuthenticatedMixin, ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        accessible_products = Product.objects.filter(owner=user)
        return Lesson.objects.filter(product__in=accessible_products).prefetch_related('product')


class ProductViewSet(IsAuthenticatedMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        # Получите доступные продукты для данного пользователя
        lesson_access_prefetch = Prefetch(
            'lessons__lessonaccess_set',
            queryset=LessonAccess.objects.filter(user=user),
            to_attr='accessible_lesson_access'
        )
        return Product.objects.filter(lessons__lessonaccess__user=user).distinct().prefetch_related(
            'lessons')


class StatisticsView(IsAuthenticatedMixin, generics.ListAPIView):

    def list(self, request):
        user_count = User.objects.count()
        product_statistics = Product.objects.annotate(
            total_lessons=Count('lessons__lessonaccess__lesson', distinct=True),
            total_completed_lessons=Count('lessons__lessonaccess', filter=Q(lessons__lessonaccess__is_completed=True)),
            total_watched_time=Sum('lessons__lessonaccess__view_time_seconds'),
            total_users=Count('lessons__lessonaccess__user', distinct=True),
            purchase_percentage=(F('total_users') * 100) / user_count
        ).values(
            'name',
            'total_completed_lessons',
            'total_watched_time',
            'total_users',
            'purchase_percentage',
        )
        return Response(product_statistics)
