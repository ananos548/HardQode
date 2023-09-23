from django.contrib import admin
from .models import Product, LessonAccess, Lesson

admin.site.register(Product)

admin.site.register(Lesson)

admin.site.register(LessonAccess)
