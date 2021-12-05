from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length = 150, null=False, blank=False)
    phone = models.PositiveBigIntegerField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length = 300)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name