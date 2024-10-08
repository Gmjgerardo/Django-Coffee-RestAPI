from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)
    capacity = models.FloatField(unique=True)

    def __str__(self) -> str:
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/coffee/")
    description = models.TextField()
    coffeeType = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.FloatField()
    rating = models.FloatField()
    reviewsCount = models.IntegerField()
    sizes = models.ManyToManyField(Size, related_name='coffees', blank=True)

    def __str__(self) -> str:
        return self.name