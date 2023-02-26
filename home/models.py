from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 300)
    email = models.EmailField(max_length = 100)
    subject = models.CharField(max_length = 500, blank = True)
    message = models.TextField()

    def __str__(self):
        return self.name



class Review(models.Model):
    name = models.CharField(max_length = 300)
    post = models.CharField(max_length = 300)
    image = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    address1 = models.CharField(max_length = 400)
    address2 = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 20)
    timing = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 300)

    def __str__(self):
        return self.address1

class Services(models.Model):
    icon = models.CharField(max_length = 500)
    title = models.CharField(max_length = 300)
    descriptions = models.TextField()

    def __str__(self):
        return self.title