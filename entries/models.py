from django.db import models
from django.utils import timezone
import datetime

FENDER = 'FND'
GIBSON = 'GIB'
GRETSCH = 'GRT'
SUHR = 'SUHR'
IBANEZ = 'IBZ'
PRS = 'PRS'
UNKNOWN = 'UKN'
EVH = 'EVH'
STRANDBERG = 'SBG'
SMITH = 'PRS'
SCHECTER = 'SHR'
TAYLOR = 'TLR'
TOM = 'AND'
MAYONES = 'MAY'
MUSIC = 'MUS'

BRAND_CHOICES = [
    ('FENDER', 'fender'),
    ('GIBSON', 'gibson'),
    ('GRETSCH', 'gretsch'),
    ('SUHR', 'suhr'),
    ('IBANEZ', 'ibanez'),
    ('PRS', 'prs'),
    ('UNKNOWN', 'unknown'),
    ('STRANDBERG', 'strandberg'),
    ('EVH', 'EVH'),
    ('SMITH', 'Paul Reed Smith'),
    ('SCHECTER', 'schecter'),
    ('TAYLOR', 'taylor'),
    ('TOM', 'tom anderson'),
    ('MAYONES', 'mayones'),
    ('MUSIC', 'music man')
]


class GuitarDeleteManager(models.Manager):
    use_for_related_fields = True

    def is_old(self, **kwargs):
        now = timezone.now()
        td = datetime.timedelta(days=30)
        timecheck = now - td

        return self.filter(date_created__lte=timecheck, **kwargs)

class GuitarInfo(models.Model):
    guitar_model = models.CharField(max_length=200)
    price = models.IntegerField()
    img_link = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=100)
    brand_choice = models.CharField(
        max_length=10,
        choices=BRAND_CHOICES,
        default=FENDER
    )
    date_created = models.DateTimeField(auto_now_add=True)

    objects = GuitarDeleteManager()

    def __str__(self):
        return self.guitar_model