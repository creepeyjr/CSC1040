from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key = True)  # Automatically increments every book with a unique id
    year = models.IntegerField()  # Years are whole integers
    author = models.CharField(max_length = 100)  # Names are strings
    price = models.DecimalField(max_digits = 6, decimal_places = 2)  # Good for currency, allows up to 9,999.99
    title = models.CharField(max_length = 200)  # Can be long paragraphs
    synopsis = models.TextField()

    def __str__(self):
        return self.title
        # Display model nicely in Django interface.