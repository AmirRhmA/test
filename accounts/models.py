from django.db import models

class Shoe(models.Model):

    name = models.CharField(max_length=50)
    price = models.FloatField()
    in_stock = models.IntegerField()
    # description = models.TextField()
    image = models.ImageField(upload_to='upload/')


    def __str__(self):
        return self.name
    