from django.db import models
class Products(models.Model):
    Name = models.CharField(max_length = 100)
    Description = models.TextField()
    Category = models.TextField()
    Price = models.IntegerField()
    Image = models.ImageField(upload_to ='pictures')
    User = models.CharField(max_length = 50)
    Contact = models.TextField()