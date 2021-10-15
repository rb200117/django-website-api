from django.urls import path
from .views import DetailSubCategory, ListCategory, DetailCategory, ListCourse, DetailCourse, ListSubCategory
urlpatterns = [
    path('categories', ListCategory.as_view(), name="categories"),
    path('categories/<int:pk>/', DetailCategory.as_view(), name="singlecategory"),
    path('subcategories', ListSubCategory.as_view(), name="subcategories"),
    path('subcategories/<int:pk>/', DetailSubCategory.as_view(), name="singlesubcategory"),
    path('courses', ListCourse.as_view(), name="courses"),
    path('courses/<int:pk>/', DetailCourse.as_view(), name="singlecourse"),

]