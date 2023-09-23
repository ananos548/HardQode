from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Lesson, LessonAccess, Product


class LessonSerializer(ModelSerializer):
    status = serializers.SerializerMethodField()
    view_time = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'video_link', 'duration_seconds', 'product', 'status', 'view_time')

    def get_status(self, obj):
        user = self.context['request'].user
        lesson_access = LessonAccess.objects.filter(user=user, lesson=obj).first()
        if lesson_access:
            view_time = lesson_access.view_time_seconds
            total_duration = obj.duration_seconds
            if view_time >= 0.8 * total_duration:
                return True
        return False

    def get_view_time(self, obj):
        user = self.context['request'].user
        lesson_access = LessonAccess.objects.filter(user=user, lesson=obj).first()
        if lesson_access:
            return lesson_access.view_time_seconds
        return 0


class LessonAccessSerializer(ModelSerializer):
    user_name = serializers.CharField(source='user.username', default='', read_only=True)
    lesson_name = serializers.CharField(source='lesson', default='', read_only=True)
    duration_seconds = serializers.CharField(source='lesson.duration_seconds', default='',
                                             read_only=True)  # длительность урока.
    products = serializers.CharField(source='lesson.product', default='', read_only=True)

    class Meta:
        model = LessonAccess
        fields = ('id', 'user_name', 'lesson_name', 'is_completed', 'view_time_seconds', 'duration_seconds', 'products')


class ProductSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'description', 'owner', 'lessons')
