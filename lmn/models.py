from django.db import models

from django.db import models
from django.contrib.auth.models import User
import datetime

# Every model gets a primary key field by default.

# Users, venues, shows, artists, notes

# User is provided by Django. The email field is not unique by
# default, so add this to prevent more than one user with the same email.
User._meta.get_field('email')._unique = True

#Require email, first name and last name
User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


""" A music artist """
class Artist(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)

    def __str__(self):
        return f'Name: {self.name}'


""" A venue, that hosts shows. """
class Venue(models.Model):
    uuid = models.CharField(max_length=200, blank=False, unique=True, default='0')
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=2, blank=False)
    zip_code = models.CharField(max_length=200, blank=False)
    thumbnail = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'Name: {self.name} Location: {self.city}, {self.state}'


""" A show - one artist playing at one venue at a particular date. """
class Show(models.Model):
    show_date = models.DateTimeField(blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f'Artist: {self.artist} At: {self.venue} On: {self.show_date}'


""" One user's opinion of one show. """
class Note(models.Model):

    STAR_RATING = (
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    )

    show = models.ForeignKey(Show, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(max_length=1000, blank=False)
    rating = models.IntegerField(choices=STAR_RATING, blank=False, default=5)
    posted_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return f'User: {self.user} Show: {self.show} Note title: {self.title} Text: {self.text} Posted on: {self.posted_date}'

