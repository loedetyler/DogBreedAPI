from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(
        "Breed", 
        on_delete=models.CASCADE,
        related_name='dogs'
        )
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Breed(models.Model):
    class SizeChoices(models.TextChoices):
        TINY = 'Tiny'
        SMALL = 'Small'
        MEDIUM = 'Medium'
        LARGE = 'Large'

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SizeChoices.choices)
    friendliness = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    trainability = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    sheddingamount = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    exerciseneeds = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name