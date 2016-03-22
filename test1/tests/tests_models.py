from django.test import TestCase
import datetime
from ..models import Musician, Album, Instrument


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

class AlbumModelTest(BaseEntries):

    def test_string_representation(self):
        self.assertEqual(str(self.album), self.album.name)

      # self.fail("TODO Test Incomplete")
# from django.db.models import CharField
# from base_tests import MusicianFactory, AlbumFactory


# class Tests():
#     # Decorator required to allow test db creation

#     @pytest.mark.django_db
#     def test_create_one_factory_user(self):
#         musician = MusicianFactory.build()
#         assert musician.first_name == 'Jim'

#     @pytest.mark.django_db
#     def test_create_one_album(self):
#         album = AlbumFactory.build()
#         musician = MusicianFactory.build()
#         musician.save()
#         # print(album.name)
#         assert album.name == "Eat A Bullet"
