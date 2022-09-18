from django.db import models

STATUS = (('active','active'), ('inactive','inactive'))

# Create your models here

class Slider(models.Model):
    heading = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media/')
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.heading

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    slug = models.CharField(max_length=100)
    level = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField()
    dis_price = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to = 'media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discription = models.TextField()
    slug = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100, choices=STATUS)
    off_percentage = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
    

