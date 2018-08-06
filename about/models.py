from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class About(models.Model):
    column = {
        ('column 1','Cột 1'),
        ('column 2','Cột 2')
    }
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = RichTextField()
    des = RichTextField(null=True)
    image = models.ImageField(upload_to='about')
    column = models.CharField(max_length=200,choices=column,default='column 1')

    def __str__(self):
        return self.name
