from django.db import models
from django.urls import reverse
from django.utils import timezone


class Event(models.Model):
    mentor = models.CharField(max_length=200)
    zoom_link = models.TextField()
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return self.mentor

    def __str__(self):
        return self.zoom_link

    def __str__(self):
        return self.start_time

    def __str__(self):
        return self.end_time

    def is_available(self):
        return (self.start_time > timezone.now and self.available)

    def has_started(self):
        return (self.start_time <= timezone.now <= self.end_date)

    def has_ended(self):
        return (self.end_time < timezone.now)

    class Meta:
        permissions = (
            ('can_edit', 'Can edit the event'),
        )

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.mentor} </a>'
