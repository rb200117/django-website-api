from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category, related_name="sub_category", on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Sub Categories"
    def __str__(self):
        return self.sub_title
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(SubCategory, related_name='courses',on_delete=models.CASCADE)
    description = models.TextField(max_length=3000,blank=True,null=True)
    language = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    duration = models.DecimalField(decimal_places=1,max_digits=3, blank=True,null=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
