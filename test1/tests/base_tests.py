import factory
import pytest
from test1.models import Musician, Album

@pytest.mark.django_db
class MusicianFactory(factory.Factory):

    class Meta:
        model = Musician

    first_name = 'Stevie'
    middle_name = 'Ray'
    last_name = 'Vaughn'
    model.save()


@pytest.mark.django_db
class AlbumFactory(factory.Factory):

    class Meta:
        model = Album

    name = 'Eat A Bullet'
    model.save()


class InstrumentFactory(factory.Factory):

    class Meta:
        model = Instrument
    instrument_type = 'Stratocaster'
