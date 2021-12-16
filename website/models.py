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

class Subscriber(models.Model):
    '''
    This newsletter system might be implemented using sendgrid (pip install sendgrid)
    When building a newsletter:
    1. A new subscriber should be able to enter their email address into a form, receive a confirmation, and click to confirm their subscription.
    2. An existing subscriber should be able to unsubscribe usng a personalized link.
    3. The admin should be able to upload ans send a file as a formatted email.
    4. The admin should access a dashboard too view subscribers and sent email.
    '''
    email = models.EmailField(unique=True, null = False, blank = False)
    conf_num = models.CharField(max_length = 15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"