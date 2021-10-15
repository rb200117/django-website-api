from rest_framework import serializers
from .models import Category, Course, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = Category
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'cat_id','sub_title')
        model = SubCategory
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'category', 'description', 'language', 'price', 'duration', 'date_created')
        model = Course

