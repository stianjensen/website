from django.db import models
from django.utils import timezone


class Door(models.Model):
    name = models.CharField(max_length=20)

    @property
    def datetime(self):
        if self.latest is None:
            return None

        return self.latest.closed or self.latest.opened

    @property
    def is_open(self):
        if self.latest is None:
            return None

        return self.latest.is_open

    @property
    def latest(self):
        if not self.data_set.exists():
            return None

        return self.data_set.order_by('-opened').first()

    def open(self):
        latest = self.latest

        if latest is not None and latest.is_open:
            return latest

        door = DoorData.objects.create(door=self, opened=timezone.now())
        door.save()

        return door

    def close(self):
        latest = self.latest

        if not latest.is_open:
            return latest

        latest.closed = timezone.now()
        latest.save()

        return latest

    def __str__(self):
        return self.name

    def get_dict(self):
        return {
            'open': self.is_open,
            'datetime': self.datetime
        }


class DoorData(models.Model):
    door = models.ForeignKey(to=Door, null=False, blank=False, db_index=True, related_name='data_set')
    opened = models.DateTimeField(null=False, blank=False, db_index=True)
    closed = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-opened',)

    @property
    def is_open(self):
        return not self.closed

    def __str__(self):
        return "{name} {status} since {datetime}".format(
            name=self.door.name,
            status='OPEN' if self.is_open else 'CLOSED',
            datetime=self.closed or self.opened
        )


def get_hackerspace_door():
    door, _ = Door.objects.get_or_create(name='hackerspace')
    return door
