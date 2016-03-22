from django.db import models


class Instrument(models.Model):
    instrument_type = models.CharField(max_length=100)
    instrument_manufacturer = models.CharField(max_length=150)
    instrument_name = models.CharField(max_length=150)

    def __str__(self):
        return instrument_type


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.ForeignKey(Instrument)

    def __str__(self):
        return self.last_name


class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
