from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m/', null=True)

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='course/%Y/%m/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class lesson(BaseModel):
    subject = models.CharField(max_length=50, null=False)
    content = models.TextField(blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject