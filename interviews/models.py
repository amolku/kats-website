""" INTERVIEWS MODEL """

from django.db import models
from django.utils import timezone

# Create your models here.


class Interview(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    picture = models.ImageField(upload_to="images/interviews/profile_pictures/", null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
