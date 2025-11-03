In the Breeds model, I was running into some troubleshooting issues. I couldn't figure out some error I was running into or wanted to verify I was on the right track since Python is not my strong suit and I was getting back into the swing of it. </br>
I gave it the requirement for setting up the Breed model and asked if I was on the right track in setting it up: </br>

> these are the requirements, </br>
> A breed should contain the following fields: </br>
> name (a character string) </br>
> size (a character string) [should accept Tiny, Small, Medium, Large] </br>
> friendliness (an integer field) [should accept values from 1-5] </br>
> trainability (an integer field) [should accept values from 1-5] </br>
> sheddingamount (an integer field) [should accept values from 1-5] </br>
> exerciseneeds (an integer field) [should accept values from 1-5] </br>
>
> does this look right in setting it up?
> ```python
> class Breed(models.Model):
>   name=models.CharField(max_length=100)
>   size = models.Choices(Tiny, Small, Medium, Large)
>   friendliness = models.IntegerChoices(1,2,3,4,5)
> ```

To which ChatGPT responded:

> You’re very close! 👏 You’ve got the right idea — just a few tweaks are needed to make it valid Django model syntax.
> Let’s go step by step.
> 🧩 The problem
> In your code:
> ```python
> size = models.Choices(Tiny, Small, Medium, Large)
> friendliness = models.IntegerChoices(1,2,3,4,5)
> ```
> *models.Choices* and *models.IntegerChoices* are meant to define enums (choice lists), not fields directly.
> You still need to define the field type (CharField, IntegerField, etc.) and then attach the choices.
> ✅ Correct Django model
> Here’s the clean, working version that satisfies your requirements:
> ```python
> from django.db import models
> class Breed(models.Model):
>   class SizeChoices(models.TextChoices):
>       TINY = 'Tiny'
>       SMALL = 'Small'
>       MEDIUM = 'Medium'
>       LARGE = 'Large'
> 
>   name = models.CharField(max_length=100)
>   size = models.CharField(max_length=10, choices=SizeChoices.choices)
>   friendliness = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
>   trainability = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
>   sheddingamount = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
>   exerciseneeds = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
> 
>   def __str__(self):
>       return self.name
> ```

I believe this was the main thing I asked ChatGPT about, I was looking back through my logs around this time and could only find this and some help with testing errors I was running into.
