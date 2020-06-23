from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=120, blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email