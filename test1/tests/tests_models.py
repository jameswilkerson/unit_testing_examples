from django.test import TestCase
import datetime
from nose.tools import nottest
from ..models import Musician, Album, Instrument


@nottest
class BaseEntries(TestCase):

    def setUp(self):
        self.instrument = Instrument(instrument_type='Guitar')
        self.instrument.save()
        self.musician = Musician(
            first_name='Jimi', last_name='Hendrix', instrument=self.instrument)
        self.musician.save()
        self.album = Album(artist=self.musician, name='Band of Gypsys',
                           num_stars=5, release_date=datetime.date(year=1970, month=3, day=25))
        self.album.save()


class MusicianModelTest(BaseEntries):

    def test_string_representation(self):
        self.assertEqual(str(self.musician), self.musician.last_name)

    def test_musician_instrument_connection(self):
        self.assertEqual(self.instrument.instrument_type,
                         self.musician.instrument.instrument_type)


class AlbumModelTest(BaseEntries):

    def test_string_representation(self):
        self.assertEqual(str(self.album), self.album.name)

    def test_album_musician_connection(self):
        self.assertEqual(self.musician.last_name, self.album.artist.last_name)


class InstrumentModelTest(BaseEntries):

    def test_string_representation(self):
        self.assertEqual(str(self.instrument.instrument_type),
                         self.instrument.instrument_type)
