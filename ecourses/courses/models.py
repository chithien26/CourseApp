from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
#cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


class User(AbstractUser):
    avatar = CloudinaryField('image')

    def __str__(self):
        return self.username

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class BaseItem(BaseModel):
    class Meta:
        abstract = True

    tags = models.ManyToManyField(Tag, blank=True)

class Category(BaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

class Course(BaseItem):
    # class Meta:
    #     unique_together = ('course','category')

    subject = models.CharField(max_length=100)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Lesson(BaseItem):
    # class Meta:
    #     unique_together = ('course', 'lesson')
    name = models.CharField(max_length=100)
    content = RichTextField()
    image = CloudinaryField('image')
    image.default = " don't know "
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Interaction(BaseModel):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Comment(Interaction):
    content = models.CharField(max_length=255)


class Like(Interaction):

    class Meta:
        unique_together = ('user', 'lesson')


