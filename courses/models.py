from django.db import models
from django.urls import reverse

class CategoryModel(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CourseModel(models.Model):
    title = models.CharField(max_length=200)
    number_of_sessions = models.PositiveIntegerField(null=True, blank=True)
    age_group = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    poster = models.ImageField(upload_to='course_posters/', null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['-category']


