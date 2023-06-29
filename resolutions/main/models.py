from django.db import models

# Create your models here.

class Format(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Resolution(models.Model):
    title = models.CharField(max_length = 1000)
    published = models.DateTimeField(auto_now_add = True, db_index = True)
    rating = models.BigIntegerField(default = 0)
    format = models.ForeignKey('Format', related_name = 'format', on_delete = models.CASCADE)
    category = models.ForeignKey('Category', related_name = 'category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title
